import csv
import sqlite3
import os

DIRNAME = os.path.dirname(__file__)
DBFILENAME = "tesla.db"

CSVFILENAME = "TSLA.csv"
DBPATH = os.path.join(DIRNAME, DBFILENAME)
CSVPATH = os.path.join(DIRNAME, CSVFILENAME)


def seed_from_csv(csvpath, dbpath):
    with open(csvpath, 'r') as csvfile, sqlite3.connect(dbpath) as connection:
        reader = csv.DictReader(csvfile)
        curs = connection.cursor()
        curs.execute("""DELETE FROM tesla1;""")

        for dictline in reader:
            SQL = """INSERT INTO tesla1(
                open,
                high,
                low,
                close,
                adjusted_close,
                volume) VALUES (?, ?, ?, ?, ?, ?);"""

            data =(dictline['open'],dictline['high'],dictline['low'],dictline['close'],
                    dictline['adjusted_close'],dictline['volume'],)

            curs.execute(SQL, data)

        

if __name__ == "__main__":
    seed_from_csv(CSVPATH, DBPATH)