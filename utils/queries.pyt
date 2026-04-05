import sqlite3
import pandas as pd

DB_PATH = "db/academico.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def carregar_dados_no_banco(csv_path):
    df = pd.read_csv(csv_path)
    conn = get_connection()
    df.to_sql("alunos", conn, if_exists="replace", index=False)
    conn.close()

def query(sql):
    conn = get_connection()
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df