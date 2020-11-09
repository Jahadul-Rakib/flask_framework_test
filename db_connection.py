# pip install mysql-connector-python

import mysql.connector

config = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root",
    database="coreapp"
)
command = config.cursor()
