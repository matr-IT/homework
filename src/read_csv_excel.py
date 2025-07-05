import pandas as pd

def read_csv(csv_path: str) -> list[dict]:
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records")

if __name__ == '__main__':
    print(read_csv('/Users/rybin/PycharmProjects/homework/data/transactions.csv'))