from sqlalchemy import create_engine

from datetime import datetime

from prefect import task, flow

import pandas as pd

@task
def load(df: pd.DataFrame, connection_string:str):

    engine = create_engine(connection_string)
    df.to_sql(f'{datetime.now()} - titanic', engine, if_exists='replace')