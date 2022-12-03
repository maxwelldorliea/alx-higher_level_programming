#!/usr/bin/python3

"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


def main():
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")

    for res in cur.fetchall():
        print(res)


if __name__ == '__main__':
    main()
