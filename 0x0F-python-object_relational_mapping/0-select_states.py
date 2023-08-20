#!/usr/bin/python3
"""Python script that lists all the states in a database named hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
"""    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close() """
