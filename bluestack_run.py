import os
import time

import mysql.connector
from appium.webdriver.appium_service import AppiumService
from pywinauto.application import Application
from appium import webdriver


appium_service = AppiumService()
appium_service.start()
port=4723
Appium_url = f"http://localhost:{port}/wd/hub"
desired_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:5565",
    "appPackage": "com.jio.bapp",
    "appActivity": "com.jio.bapp.activity.SplashActivity",
    "noReset": "True",
    "idleTimeout": 60000
}
app = Application(backend='uia').start(r'"C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Nougat32_1')  # --instance Nougat64 --cmd launchApp --package "in.co.metro.customerappmetro')
print("done")
os.system("adb connect 127.0.0.1:5565")
driver = webdriver.Remote(Appium_url, desired_caps)
sql_con = mysql.connector.connect(host="192.168.100.55", user="root", password="xbyte", database="jio_mart_chennai")
sql_cursor = sql_con.cursor()
sql_cursor.execute("select count(*) from jio_mart_chennai_01_11_csv where status='pending'")#<-----------------------
data = int(sql_cursor.fetchone()[0])
print('count: ',data)
while data!=0:
    os.system("python jio_mart_data.py")
appium_service.stop()
