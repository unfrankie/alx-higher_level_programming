#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument safely from MySQL injection
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         db=database,
                         port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                   (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
