# coding=utf-8
import mysql.connector
import xlsxwriter
from query import q, table,columns
from letters import letters
import string
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '/config.json', "r") as json_data_file:
    conf = json.load(json_data_file)

conn = mysql.connector.connect(**conf)
cur = conn.cursor()
cur.execute("set innodb_lock_wait_timeout=100;")
q_describe = "describe " + table + ";"
cur.execute(q_describe)
bdescribe = cur.fetchall()
wb = xlsxwriter.Workbook('test.xlsx')
ws = wb.add_worksheet()
col = 0

for bdes_row in bdescribe:
    ws.write(string.upper(letters[col] + str(1)), bdes_row[0])
    col += 1
num1 = 2
col = 0
num = 1

cur.execute(q)
data = cur.fetchall()
for row in data:
    col = 0
    for line in range(len(row)):
        l = letters[col] + str(num1)
        ws.write(string.upper(l), row[line])
        col += 1
    num1 += 1

wb.close()
