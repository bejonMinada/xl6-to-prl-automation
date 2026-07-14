import os
import pandas as pd
import sys
from datetime import datetime

def convert(input_file, output_file):
    try:
        df = pd.read_excel(input_file, engine="openpyxl")
    except Exception:
        df = pd.read_csv(input_file)

    lines = [
        "# PRL FILE GENERATED",
        f"# Source: {input_file}",
        f"# Generated: {datetime.now()}",
        ""
    ]

    for i, row in df.iterrows():
        lines.append(f"[RECORD_{i+1}]")
        for col in df.columns:
            lines.append(f"{col}={row[col] if pd.notna(row[col]) else ''}")
        lines.append("")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])