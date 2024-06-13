from tkinter.messagebox import*

import sqlite3

con=sqlite3.Connection('bus_booking_database')

cur=con.cursor()
cur.execute('select * from operator')
r=cur.fetchall()
print(r)
