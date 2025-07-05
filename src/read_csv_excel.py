import pandas as pd

def read_csv(csv_path: str) -> list[dict]:
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records", delimeter=";")
