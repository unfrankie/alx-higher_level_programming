#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3], charset="utf8")
    cursor = datab.cursor()
    cmd = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(cmd)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    datab.close()
