import psycopg2
import pandas as pd
import os


def check_state(df):
    """
    Check if column state has a lengt of two and
    just have letters

    Arguments:
       df: a dataframe
    Returns:
       A validated dataframe
    """

    df2 = df[df["state"].apply(lambda x: len(str(x))) == 2]
    if df2.shape[0] != df.shape[0]:
        res = df.shape[0] - df2.shape[0]
        print("Drop ", str(res), "rows in validation state lenght")

    df3 = df2[~df2["state"].str.contains("[^A-Za-z\s]")]

    if df3.shape[0] != df2.shape[0]:
        res = df2.shape[0] - df3.shape[0]
        print("Drop ", str(res), "rows in validation state type")

    print("Validation of state column")
    return df3


def get_columns_csv(columns_df):
    """
    Get columns to later validate with postgres
    Arguments:
      df: a dataframe
    Returns
      List with column names with the serial id
    """
    columns = columns_df.values.tolist()
    # incremental variable
    columns.append("user_id")
    columns.sort()
    return columns


def connection_postgresql():
    """
    Connection to postgresql

    Returns:
      The connection and the cursor
    """
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="example",
        host="127.0.0.1",
        port="5432",
    )
    cur = conn.cursor()
    return conn, cur


def check_schemas(cur, columns):
    """
    Validate csv and postgres table has the same columns

    Arguments:
      cur: a cursor from psycopg2
      columns: a list

    Returns:
      Boolean of the validation
    """
    sql_schema = """select column_name from 
                    information_schema.columns 
                    where table_name = 'accounts'
                    group by column_name
                    order by column_name"""
    cur.execute(sql_schema)
    columns_post = []
    for i in cur.fetchall():
        columns_post.append(i[0])

    if columns == columns_post:
        return True
    return False


def insert_rows(df3, cur, conn):
    """ "
    Insert rows from a dataframe

    Arguments:
      df3: a dataframe
      cur: a cursor from psycopg2
      conn: a connection from psycopg2

    """
    # Create a list of tupples
    tuples = [tuple(x) for x in df3.to_numpy()]
    cols = ",".join(list(df3.columns))

    query = (
        "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,\
        %%s, %%s, %%s, %%s, %%s, %%s, %%s, %%s)"
        % ("accounts", cols)
    )
    try:
        cur.executemany(query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cur.close()
    print("execute done")
    cur.close()


file = pd.read_csv("../Sample.csv")
conn, cur = connection_postgresql()
columns = get_columns_csv(file.columns)

df3 = check_state(file)

validation = check_schemas(cur, columns)

if validation == True:
    insert_rows(df3, cur, conn)

else:
    print("Check schema validation: ", columns)
