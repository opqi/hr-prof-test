#!/usr/bin/env python
import pandas as pd
from sqlalchemy import create_engine

uri = 'postgresql://myuser:mypassword@localhost:5432/mydatabase'

engine = create_engine(uri)


def init_db():
    conn = engine.connect()

    file_path = './data/test_data_clean.csv'
    data = pd.read_csv(file_path, low_memory=False)

    table_name = 'hr_prof_data'

    data.Date = pd.to_datetime(data.Date)
    data.FederalDistrict_Name = data.FederalDistrict_Name.apply(
        lambda x: x[:-1])

    data.to_sql(table_name, conn,
                if_exists='append', index=False,
                chunksize=1000, method='multi')

    conn.close()


if __name__ == '__main__':
    init_db()
