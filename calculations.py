import pandas as pd
import logging

def calc_profit(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate profit and add to dataframe"""
    df["Totals.Profit"] = df["Totals.Revenue"] - df["Totals.Expenditure"]
    logging.info("Added Totals.Profit column")
    return df

def calc_roi(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate roi to the nearest hunderth and add to dataframe"""
    df["Totals.ROI"] = round(df["Totals.Revenue"] / df["Totals.Expenditure"],2)
    logging.info("Added Totals.ROI column")
    return df

def greatest_profit(df: pd.DataFrame):

    """Calculate which state and year combination had the greatest profit"""

    df = df.loc[df["Totals.Profit"].idxmax()]
    return df["State"], int(df["Year"])

def greatest_roi(df: pd.DataFrame):

    """Calculate which state and year combination had the greatest profit"""

    df = df.loc[df["Totals.ROI"].idxmax()]
    return df["State"], int(df["Year"])