import psycopg2
from config.settings import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT


def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )


def execute_query(query, params=None, fetch=False):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query, params or ())

        if fetch:
            result = cursor.fetchall()
        else:
            conn.commit()
            result = None

        return result

    finally:
        cursor.close()
        conn.close()