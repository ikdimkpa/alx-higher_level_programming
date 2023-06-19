#!/usr/bin/python3
import MySQLdb
import sys

# Get the MySQL username, password, database name, and state name from command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

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

# Execute the query to retrieve states matching the input name
query = "SELECT * FROM states WHERE name = %s ORDER BY id"
cursor.execute(query, (state_name,))

# Fetch all the rows returned by the query
rows = cursor.fetchall()

# Print the states in the desired format
for row in rows:
    print(row)

# Close the cursor and database connection
cursor.close()
connect_db.close()