import pandas as pd


def load_sql(min_sender=100):
    con = "mysql+mysqldb://root:@127.0.0.1:" f"3306/enron"
    msg = pd.read_sql_query(
        f"""SELECT sender, body FROM  message
    WHERE sender IN(
    SELECT DISTINCT sender
    FROM message
    GROUP BY sender
    HAVING COUNT(*)>{min_sender}
    )""",
        con,
    )
    return msg
