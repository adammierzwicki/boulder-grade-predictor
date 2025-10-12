import os
import sqlite3

import pandas as pd

DB_PATH = './db/db-320.sqlite3'
OUT_DIR = './out'


def export_tables(db_path, out_dir):
    connection = sqlite3.connect(db_path)

    table_names = [table[0] for table in connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table'")]
    print('Tables:', table_names)

    for table in table_names:
        df = pd.read_sql_query(f'SELECT * FROM {table}', connection)
        df.to_csv(f'{out_dir}/{table}.csv', index=False)

    connection.close()


if __name__ == '__main__':
    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)
    export_tables(DB_PATH, OUT_DIR)
