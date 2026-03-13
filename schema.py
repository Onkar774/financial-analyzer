import datetime
import pandas as pd
import datetime
from pathlib import Path

BASEPATH = Path(__file__).resolve().parent
RAWDATA = BASEPATH / "data" / "finance.csv"

EXPECTED_COLS = ["State","Year","Totals.Capital outlay","Totals.Revenue","Totals.Expenditure","Totals.General expenditure",
                 "Totals.General revenue","Totals.Insurance trust  revenue","Totals.Intergovernmental","Totals.License tax",
                 "Totals.Selective sales tax","Totals.Tax","Details.Correction.Correction Total","Details.Education.Education Total",
                 "Details.Financial Aid.Assistance and Subsidies","Details.Financial Aid.Cash and Securities Total","Details.Health.Health Total Expenditure",
                 "Details.Intergovernmental.Intergovernmental Expenditure","Details.Intergovernmental.Intergovernmental to Combined and Unallocable","Details.Natural Resources.Natural Resources Construction",
                 "Details.Utilities.Utilities Current Operation","Details.Welfare.Welfare Institution Total Expenditure","Details.Natural Resources.Parks.Parks Total Expenditure","Details.Transportation.Highways.Highways Total Expenditure",
                 "Totals. Debt at end of fiscal year","Details.Insurance benefits and repayments","Details.Interest on debt","Details.Interest on general debt","Details.Miscellaneous general revenue","Details.Other taxes","Details.Police protection"
                 ]

def enforce_schema(df: pd.DataFrame) -> pd.DataFrame:
    # Check for columns
    missing = [c for c in EXPECTED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    
    # Drop rows with any NaNs
    df = df.dropna(subset=EXPECTED_COLS).copy()

    return df

def dedupe(df: pd.DataFrame) -> pd.DataFrame:
    """Drop potential duplicates from the dataframe"""
    return df.drop_duplicates()

def time_now() -> str:

    return datetime.datetime.now()
