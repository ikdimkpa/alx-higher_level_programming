#!/usr/bin/python3
"""Python script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities as c\
                                inner join states as s\
                                                    ON c.state_id = s.id\
                                         WHERE s.name = %s", argv[4])

    cities = cursor.fetchall()

    for city in cities:
        print(", ".join(city[1]))

    cursor.close()
    db.close()
