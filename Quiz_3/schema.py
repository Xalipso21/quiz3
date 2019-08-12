import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'tesla.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        SQL = "DROP TABLE IF EXISTS tesla1;"
        cur.execute(SQL)

        SQL = """ CREATE TABLE tesla1(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            adjusted_close FLOAT,
            volume INTEGER
            
        ); """
        cur.execute(SQL)