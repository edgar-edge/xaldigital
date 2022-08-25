from sqlite3 import DatabaseError
import psycopg2
from psycopg2 import DatabaseError

def get_connection():
    try:
        return psycopg2.connect(
        database="postgres",
        user="postgres",
        password="example",
        host="127.0.0.1",
        port="5432",
    )
    except DatabaseError as ex:
        raise ex
