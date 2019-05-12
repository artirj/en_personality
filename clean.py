from load import load_sql

# Cleaning
def no_forward(df):
    return df[~df.body.str.startswith("---------------------- Forwarded by")]


def no_original_msg(df):
    df = df.copy()
    exprs = [
        "-----Original Message",
        "---------------------- Forwarded by",
        "----- Forwarded by",
        "-------- Inline attachment follows",
        "\t\t\tFrom:",
        "cc: Subject:",
        "Sara ShackletonEnron North America Corp",
        " Debra PerlingiereEnron",
        "Outlook Migration Team",
        "Matthew B Fleming@",
        "Lynn Lynn Blair Northern",
        "TASK ASSIGNMENT",
        "X-FileName",
        "KayRhonda L Denton@ECT0",
    ]
    # Find emails to drop
    drop_emails = (
        df.body.str.extract('("?[A-z \.,]+"? <[a-zA-Z0-9_.]+@[A-z ]+\..{2,3}>)')[0]
        .dropna()
        .unique()
        .tolist()
    )
    exprs += drop_emails
    drop_emails2 = (
        df.body.str.extract("((?:From:)? [A-z ]+@[A-Z]{1,7})").dropna()[0].unique().tolist()
    )
    exprs += drop_emails2
    drop_emails3 = (
        df.body.str.extract("([0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2} PM(?: )?To:)")
        .dropna()[0]
        .unique()
        .tolist()
    )
    exprs += drop_emails3
    for expr in exprs:
        mask = df.body.str.contains(expr, regex=False)

        df.loc[mask, "body"] = df.loc[mask, "body"].apply(lambda x: x.split(expr)[0])
    return df


def remove_words(df):
    df = df.copy()
    reg = {
        "--------------------------Sent from my BlackBerry Wireless Handheld \(www\.BlackBerry\.net\)": "",
        "\t": " ",
        " +": " ",
    }
    for exp, replace in reg.items():
        df["body"] = df.body.str.replace(exp, replace, regex=True)
    return df


def remove_blank(df):
    df["body"] = df["body"].str.strip()
    return df[df.body.str.len() >= 2]


def process_df(df):
    return df.pipe(no_forward).pipe(no_original_msg).pipe(remove_words).pipe(remove_blank)


def load_clean_data(min_sender=100):
    data = load_sql(min_sender)
    return data.pipe(process_df)
