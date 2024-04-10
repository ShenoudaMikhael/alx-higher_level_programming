#!/usr/bin/python3
"""Filter states Module"""
import sys
import MySQLdb

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.name FROM cities
        join states on cities.state_id = states.id where states.name = %s
        ORDER BY cities.id ASC""",
        (sys.argv[4],),
    )  # HERE I have to know SQL to grab all states in my database
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row[0], end="\n" if query_rows[-1] == row else ", ")
    cur.close()
    conn.close()
