#!/usr/bin/python3
"""Module to select rows with name starting with N"""

import MySQLdb
import sys

if __name__ == '__main__':
    connect = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = connect.cursor()
    query = "SELECT * FROM states WHERE `name` LIKE BINARY" \
            "'N%' ORDER BY id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    connect.close()
