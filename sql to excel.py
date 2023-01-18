# import pymysql
# import pandas as pd
# import csv
# import openpyxl
# try:
#     db_host = "192.168.1.89"
#     db_user = "root"
#     db_password = "xbyte"
#     db_name = "jio_mart_chennai"
#     db_table = "exact_match_chennai"
#     con = pymysql.connect(db_host,db_user, db_password, db_name)
#     cursor = con.cursor()
#     sql = f"select * from  {db_table}"
#     df = pd.read_sql(sql,con)
#     df.to_csv('jio_mart_chennai_01_11.csv',encoding='utf-8')
# except Exception as e:
#     print(e)