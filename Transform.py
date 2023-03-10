from Extract import read_data
from Load import load

from prefect import flow, task

import pandas as pd
import numpy as np

@task
def add_surname(df: pd.DataFrame):
    df['Surname'] = df['Name'].apply(lambda x: x.split(',')[0])
    return df

@task
def add_title(df: pd.DataFrame):
    df['Title'] = df['Name'].apply(lambda x: x.split(',')[1].split('.')[0].replace(' ',''))
    return df

@task
def fill_embarked(df: pd.DataFrame):
    df['Embarked'] = df['Embarked'].fillna('S')
    return df

@task
def fillAge(df:pd.DataFrame): ## title
    start = df.groupby(['Sex','Pclass'])[['Age']].agg(lambda x: x.mean() + x.std()) ##.unstack()
    end = df.groupby(['Sex','Pclass'])[['Age']].agg(lambda x: x.mean() - x.std()) ##.unstack()

    _list = ['female','male']
    for i in _list:
        for j in range(3):
            x = start.loc[i].iloc[j].values[0]
            y = end.loc[i].iloc[j].values[0]
            length = len(df[df['Sex'] == i][df['Pclass'] == (j+1)][np.isnan(df['Age'])]) 
            index = df[df['Sex'] == i][df['Pclass'] == (j+1)][df['Age'].isna()].index
            random_values = np.random.randint(y,x,length)
            df['Age'].loc[index] = random_values

    df['Age'] = df['Age'].astype(int)

    return df

@flow
def main(path='data/titanic.csv', connection_string='postgresql://root:root@localhost:5432/load'):
    df = read_data(path)
    df = add_surname(df)
    df = add_title(df)
    df = fill_embarked(df)
    df = fillAge(df)
    load(df, connection_string)

if __name__ == '__main__':
    main()