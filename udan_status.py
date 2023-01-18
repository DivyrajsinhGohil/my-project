if __name__ == '__main__':

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

    host = '192.168.100.89'
    port_m = '27017'
    db = 'Udaan_ahmedabad'
    con = pymongo.MongoClient(f'mongodb://{host}:{port_m}/')
    mydb = con[db]
    today_date_z = datetime.now().date()
    var = 'Udaan_Product_ahmedabad_15_12_2022'  # new table
    conn = mydb[var]
    sql_con = mysql.connector.connect(host="192.168.100.89", user="root", password="xbyte", database="udaan_2022")
    sql_cursor = sql_con.cursor()
    var1=conn.find()
    for links in var1:
        JPIN = links['JPIN']

        try:
            sql_cursor.execute(
                f"update udaan_ahmedabad set status = 'done' where jpin = '{JPIN}'")
            sql_con.commit()
            print("sql status updated - ", JPIN)
        except Exception as e:
            print(e, "error in update status in sql -",JPIN)