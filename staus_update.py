import re
import dropbox
import mysql.connector
import datetime
import os
import time
from time import sleep
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import pymongo
from datetime import datetime

host = 'localhost'
port_m = '27017'
db = 'jiomart_chennai'
con = pymongo.MongoClient(f'mongodb://{host}:{port_m}/')
mydb = con[db]
today_date_z = datetime.now().date()
var = f'{today_date_z}_jio_mart'  # new table
conn = mydb[var]
sql_con = mysql.connector.connect(host="192.168.100.55", user="root", password="xbyte", database="jio_mart_chennai")
sql_cursor = sql_con.cursor()
var=conn.find()
for links in var:
    JPIN = links['JPIN']

    try:
        sql_cursor.execute(
            f"update jio_mart_chennai.jio_mart_chennai_01_11_csv set status = 'done' where jpin = '{JPIN}'")
        sql_con.commit()
        print("sql status updated - ", JPIN)
    except Exception as e:
        print(e, "error in update status in sql -",JPIN)