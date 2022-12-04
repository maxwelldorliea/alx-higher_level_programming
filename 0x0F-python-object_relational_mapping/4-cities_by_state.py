#!/usr/bin/python3
"""Lsts all cities from the database hbtn_0e_4_usa."""

import MySQLdb
from sys import argv as arg


def main():
    conn = MySQLdb.connect(
            host='localhost', port=3306, user=arg[1], passwd=arg[2], db=arg[3])
    cur = conn.cursor()
    cur.execute("""
    SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id
    """)

    for res in cur.fetchall():
        print(res)


if __name__ == '__main__':
    main()
