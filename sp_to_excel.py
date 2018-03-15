# coding=utf-8
import mysql.connector
import xlsxwriter
from query import sp, arg
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

wb = xlsxwriter.Workbook('testSP.xlsx')
ws = wb.add_worksheet()
num = 1
num1 = 2
cur.callproc(sp, arg)
for row in cur.stored_results():
    col1 = 0
    for clnames in row.description:
        l = letters[col1] + str(num)
        ws.write(string.upper(l), clnames[0])
        col1 += 1
    for line in row.fetchall():
        col = 0
        for lll in line:
            l = letters[col] + str(num1)
            ws.write(string.upper(l), lll)
            col += 1
        num1 += 1
wb.close()
