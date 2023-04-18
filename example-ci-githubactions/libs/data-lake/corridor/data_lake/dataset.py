import io
import random

import pandas as pd
import pkg_resources


class Dataset:
    def __init__(self, name: str) -> None:
        self.name = name

    def read(self) -> pd.DataFrame:
        raw_data = io.BytesIO(
            pkg_resources.resource_string(__name__, "home_ownership.csv")
        )
        return pd.read_csv(raw_data)

    def generate_random(self) -> pd.DataFrame:
        df = self.read()
        for colname, coltype in dict(df.dtypes).items():
            if isinstance(coltype, int):
                # Generate a column with random numbers and replace the values
                random_col = [
                    random.randint(df[colname].min(), df[colname].max())
                    for _ in range(df.length)
                ]
                df[colname] = random_col

        return df
