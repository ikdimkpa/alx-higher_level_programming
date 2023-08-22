#!/usr/bin/python3
""""""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities as c inner join states as s\
            ON c.state_id = s.id")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()

