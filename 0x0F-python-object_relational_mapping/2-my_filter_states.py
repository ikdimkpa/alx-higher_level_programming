#!/usr/bin/python3
"""Module to collect filter input"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT * " \
            "FROM states " \
            "WHERE name " \
            "LIKE BINARY '{}' " \
            "ORDER BY states.id ASC".format(sys.argv[4])
    cur.execute(query)
    query_all_rows = cur.fetchall()
    for row in query_all_rows:
        print(row)
    cur.close()
    conn.close()
