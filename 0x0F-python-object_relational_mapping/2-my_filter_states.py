#!/usr/bin/python3

"""
Lists all values in the states.
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv as arg


def main():
    conn = MySQLdb.connect(
            host='localhost', port=3306, user=arg[1], passwd=arg[2], db=arg[3])

    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM states WHERE BINARY name
    LIKE '{}' ORDER BY states.id
    """.format(arg[4]))

    for res in cur.fetchall():
        print(res)


if __name__ == '__main__':
    main()
