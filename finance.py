from lineage import *
from pathlib import Path


BASEPATH = Path(__file__).resolve().parent
RAWDATA = BASEPATH / "data" / "finance.csv"

def main():    
    out = run_pipeline(RAWDATA)

    for ev in out["lineage"]:
        with open("lineage.log", "a") as f:
            f.write(f"{ev.timestamp} | {ev.step:7s} | in={ev.input_rows:5d} | out={ev.output_rows:5d} | +{ev.columns_added} -{ev.columns_removed} | {ev.description}")
            f.write("\n")

if __name__ == "__main__":
    main()