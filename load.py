import pandas as pd


def load_sql(min_sender=100):
    """
    We load only frequent messages to have a sufficient corpus per employee.
    Also, load only employees (that exist in employee tables)
    Not corporate accounts (comms, etc)
    """
    con = "mysql+mysqldb://root:@127.0.0.1:" f"3306/enron"
    msg = pd.read_sql_query(
        f"""SELECT sender,body FROM
        (SELECT sender, body FROM  message
        WHERE sender IN(
        SELECT DISTINCT sender
        FROM message
        GROUP BY sender
        HAVING COUNT(*)>{min_sender}
        ) ) AS tab
        INNER JOIN
        employeelist
        ON employeelist.Email_id=tab.sender""",
        con,
    )
    return msg
