#!/usr/bin/python3

# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect(
    db='test',
    user='root',
    password='password',
    host='localhost')
c = conn.cursor()

# # Insert some example data.

# c.execute("INSERT INTO user VALUES (1,'saji','palamanna')")
# conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM user")
print([(r[0], r[1],r[2]) for r in c.fetchall()])



