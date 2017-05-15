#!/usr/bin/env python

import sqlite3
import datetime

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

for row in c.execute("select * from app1_certificateinfo"):
    print row


for row in c.execute("select certName, expiryDate, reminder, escalationMail from app1_certificateinfo"):
    print row


print datetime.datetime.today()

print datetime.datetime.strptime("2015-01-30", "%Y-%m-%d")

(date1-date2).days
