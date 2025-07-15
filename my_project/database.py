import psycopg2
from contextlib import contextmanager

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="dbt",
        user="postgres",
        password="admin3542"
    )
    return conn

@contextmanager
def get_db():
    conn = get_db_connection()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
