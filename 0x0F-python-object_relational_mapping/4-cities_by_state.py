#!/usr/bin/python3
import MySQLdb
import sys

# Get the MySQL username, password, and database name from command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL server
if __name__ == '__main__':
    connect_db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

# Create a cursor object to execute SQL queries
cursor = connect_db.cursor()

# Execute the query to retrieve all cities
query = "SELECT * FROM cities ORDER BY id"
cursor.execute(query)

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Print the cities in the desired format
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
connect_db.close()
