from pathlib import Path
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(level= logging.INFO)

def load(source: Path) -> pd.DataFrame:
    """Load csv file and generate a dataframe"""

    logger.info("Loading finance.csv")
    df = pd.read_csv(source)
    logger.info("%s rows and %s columns loaded", df.shape[0], df.shape[1])

    return df