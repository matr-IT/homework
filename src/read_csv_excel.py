import pandas as pd


def read_csv(csv_path: str) -> list[dict]:
    """Function reads csv-files and returns list of dicts"""
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records")


def read_excel(csv_path: str) -> list[dict]:
    """Function reads excel-files and returns list of dicts"""
    df = pd.read_excel(csv_path)
    return df.to_dict(orient="records")
