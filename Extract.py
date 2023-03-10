import pandas as pd

from prefect import task, flow

@task
def read_data(path:str):
    df = pd.read_csv(path)
    return df