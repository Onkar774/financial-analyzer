import pandas as pd
from loader import load
from schema import enforce_schema, time_now
from calculations import *
from dataclasses import dataclass
from typing import List, Dict
from pathlib import Path
import sqlite3



@dataclass
class LineageEvent:
    step: str
    description: str
    timestamp: str
    input_rows: int
    output_rows: int
    columns_added: List[str]
    columns_removed: List[str]

def run_pipeline(source: Path) -> Dict[str, object]:
    lineage: List[LineageEvent] = []

    # Extract
    raw = load(source)
    lineage.append(LineageEvent(
        step="extract",
        description="Loading CSV as string",
        timestamp=time_now(),
        input_rows=0,
        output_rows=len(raw),
        columns_added=[],
        columns_removed=[]
    ))

    # Schema checks
    clean = enforce_schema(raw)
    lineage.append(LineageEvent(
        step="validate",
        description="Enforce schema",
        timestamp=time_now(),
        input_rows=len(raw),
        output_rows=len(clean),
        columns_added=[],
        columns_removed=[]
    ))


    # Derived Column
    with_profit = calc_profit(raw)
    lineage.append(LineageEvent(
        step="derive Totals.Profit",
        description="Added profit (Revenue - Expenditure)",
        timestamp=time_now(),
        input_rows=len(raw),
        output_rows=len(with_profit),
        columns_added=["Totals."],
        columns_removed=[]
    ))

    # Derived Column
    with_roi = calc_roi(with_profit)
    lineage.append(LineageEvent(
        step="derive Totals.ROI",
        description="Added ROI (Revenue / Expenditure)",
        timestamp=time_now(),
        input_rows=len(with_profit),
        output_rows=len(with_roi),
        columns_added=["Totals.ROI"],
        columns_removed=[]
    ))

    # SQL Segment
    
    con = sqlite3.connect("finance.db")
    cur = con.cursor()
    
    with_roi.to_sql("finance", con, if_exists="replace", index=False)

    table = pd.read_sql("SELECT * FROM finance", con)
    print(time_now())
    print(table)

    # Analytics
    max_profit = greatest_profit(with_roi)
    print(f"The state with the greatest profit is {max_profit}")

    max_roi = greatest_roi(with_roi)
    print(f"The state with the greatest ROI is {max_roi}")

    return {
        "lineage": lineage,
        }