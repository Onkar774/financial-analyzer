from pathlib import Path
import logging
import pandas as pd
from finance import BASEPATH
import datetime

pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 2000)


logger = logging.getLogger(__name__)
logging.basicConfig(filename="log.log", level= logging.INFO)

with open("log.log", "a") as f:
  f.write(str(datetime.datetime.now()))
  f.write("\n")

def load(source: Path) -> pd.DataFrame:
    """Load csv file and generate a dataframe"""

    logger.info("Loading finance.csv")
    df = pd.read_csv(source)
    logger.info("%s rows and %s columns loaded", df.shape[0], df.shape[1])

    return df