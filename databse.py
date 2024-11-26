import fdb
import os
from dotenv import load_dotenv

load_dotenv()

DSN_CONFIG = os.getenv('DSN_CONFIG')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
CHARSET = os.getenv('CHARSET')

DSN_BRANCH = os.getenv('DSN_BRANCH')


def get_db_myconfig():

    con = fdb.connect(
        dsn=DSN_CONFIG,
        user=USER,
        password=PASSWORD,
        charset=CHARSET
        )

    cur = con.cursor()

    return cur

def get_db(dbname:str):
    con = fdb.connect(
        dsn=DSN_BRANCH.format(dbname) if dbname != 'office' else DSN_BRANCH,
        user=USER,
        password=PASSWORD,
        charset=CHARSET
        )
    cur = con.cursor()
    return cur


