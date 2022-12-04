#!/usr/bin/python3
"""Lsts all cities from the database hbtn_0e_4_usa."""

import MySQLdb
from sys import argv as arg


def main():
    conn = MySQLdb.connect(
            host='localhost', port=3306, user=arg[1], passwd=arg[2], db=arg[3])
    cur = conn.cursor()
    cur.execute("""
    SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %(sname)s
    ORDER BY cities.id
    """, {'sname': arg[4]})

    result = cur.fetchall()
    for res in result:
        print(res[0], end='')
        if res != result[-1]:
            print(', ', end='')
    print()


if __name__ == '__main__':
    main()
