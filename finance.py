from lineage import *


BASEPATH = Path(__file__).resolve().parent
RAWDATA = BASEPATH / "data" / "finance.csv"

def main():    
    out = run_pipeline(RAWDATA)

    print("===== DATA LINEAGE ======")
    for ev in out["lineage"]:
        print(f"{ev.timestamp} | {ev.step:7s} | in={ev.input_rows:5d} | out={ev.output_rows:5d} | +{ev.columns_added} -{ev.columns_removed} | {ev.description}")

if __name__ == "__main__":
    main()