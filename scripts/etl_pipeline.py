"""
ETL pipeline for RTA Accident Analysis Project.

This script adapts the NST DVA starter template for the Road Traffic Accident dataset.
It performs basic cleaning, standardization, and light feature engineering,
then exports a processed dataset for notebook analysis and Tableau dashboards.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd
import numpy as np


# ─── Normalize Columns ──────────────────────────────────────────────────────
def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )
    df.columns = cleaned
    return df


# ─── Basic Cleaning ─────────────────────────────────────────────────────────
def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    df = normalize_columns(df)

    # Standardize missing values
    missing_values = ["unknown", "Unknown", "NA", "-", ""]
    df = df.replace(missing_values, np.nan)

    # Fill missing values
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna(df[col].mode()[0]).str.strip().str.lower()
        else:
            df[col] = df[col].fillna(df[col].median())

    # Convert types
    df["number_of_casualties"] = pd.to_numeric(df["number_of_casualties"], errors="coerce")
    df["time"] = pd.to_datetime(df["time"], errors="coerce")

    # Remove invalid + duplicates
    df = df[df["number_of_casualties"] >= 0]
    df = df.drop_duplicates().reset_index(drop=True)

    return df


# ─── Feature Engineering (LIGHTWEIGHT) ──────────────────────────────────────
def add_features(df: pd.DataFrame) -> pd.DataFrame:

    # Hour + Time Period
    df["hour"] = df["time"].dt.hour

    def get_time_period(h):
        if pd.isna(h):
            return "unknown"
        if h < 6:
            return "night"
        elif h < 12:
            return "morning"
        elif h < 18:
            return "afternoon"
        else:
            return "evening"

    df["time_period"] = df["hour"].apply(get_time_period)

    # Severity Score
    severity_map = {
        "slight injury": 1,
        "serious injury": 2,
        "fatal injury": 3
    }
    df["severity_score"] = df["accident_severity"].map(severity_map)

    # Weekend flag
    df["is_weekend"] = df["day_of_week"].isin(["saturday", "sunday"])

    return df


# ─── Build Dataset ──────────────────────────────────────────────────────────
def build_dataset(input_path: Path) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    df = basic_clean(df)
    df = add_features(df)
    return df


# ─── Save Output ────────────────────────────────────────────────────────────
def save_processed(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


# ─── CLI ────────────────────────────────────────────────────────────────────
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run RTA ETL pipeline")
    parser.add_argument("--input", required=True, type=Path, help="Path to raw CSV")
    parser.add_argument("--output", required=True, type=Path, help="Path to processed CSV")
    return parser.parse_args()


# ─── Main ───────────────────────────────────────────────────────────────────
def main() -> None:
    args = parse_args()
    df = build_dataset(args.input)
    save_processed(df, args.output)

    print(f"Processed dataset saved to: {args.output}")
    print(f"Rows: {len(df)} | Columns: {len(df.columns)}")


if __name__ == "__main__":
    main()