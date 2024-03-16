#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument safely from MySQL injection
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3], charset="utf8")
    cursor = datab.cursor()
    cmd = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    state = argv[4]
    cursor.execute(cmd, (state,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    datab.close()
