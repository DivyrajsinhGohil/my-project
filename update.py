from mysql.connector import errorcode
import mysql.connector
import pandas as pd

create_conn = mysql.connector.connect(
            host="192.168.100.55",
            user="root",
            password="xbyte",
            database="jio_mart_chennai"
        )
curr = create_conn.cursor()
curr.execute("update jio_mart_chennai_01_11_csv set status = 'Pending'")
create_conn.commit()
print("status updated")