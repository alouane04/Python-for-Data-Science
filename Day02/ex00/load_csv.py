import pandas as pd


def load(path: str) -> pd.DataFrame:
    """writes the dimensions of the data set
        and returns it"""

    try:
        df = pd.read_csv(path)

        print("Loading dataset of dimensions", df.shape)

        return df
    except Exception as e:
        print(e)
        return None
