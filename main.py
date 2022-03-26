from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv
from queries import create_table_query,aggregate_query
import pandas as pd
from transform import main_df

load_dotenv()

HOST = getenv('host')
USER = getenv('user')
PASSWORD = getenv('password')
NAME = getenv('dbname')
PORT = getenv('port')


def get_engine(dbname, user, password, host, port):

    URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(URL)
    return engine


engine = get_engine(NAME, USER, PASSWORD, HOST, PORT)


def load_data(engine,df):
    with engine.begin() as connection:
        df.to_sql('dealer_data', con=connection,
                       if_exists='append', index=False)


def query(engine,query):
    with engine.begin() as connection:
        agg_data=connection.execute(query)
    return agg_data


if __name__ == '__main__':
    load_data(engine,main_df)
    data=query(engine,aggregate_query)
    pd.DataFrame(data).to_csv('output/agg_data.csv', index=False)