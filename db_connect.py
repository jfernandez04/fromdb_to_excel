# coding=utf-8
import mysql.connector
import xlsxwriter
from query import q, table
from letters import letters
import string
import json

with open('config.json') as json_data_file:
    conf = json.load(json_data_file)
# print(conf)
conn = mysql.connector.connect(**conf)
cur = conn.cursor()
# q = "select * from base_banco"

q_describe = "describe " + table
cur.execute(q)
rows = cur.fetchall()

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
for row in rows:
    col = 0
    for ab in row:
        ws.write(string.upper(letters[col] + str(num1)), ab)
        col += 1
    num1 += 1

wb.close()
