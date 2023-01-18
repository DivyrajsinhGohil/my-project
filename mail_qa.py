import json
import shutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mysql.connector
import pandas as pd
from datetime import datetime, timedelta
import socket
from json2html import *
import numpy as np
import dropbox
# import datetim
import pymongo
import os

access_token = 'Mw46Be7ueY4AAAAAAAAAAU00jILbPUEiwLeAT38dKe2r4RagMsmHZykPizAFE8VB'
File_Name = f"{datetime.now().date()}_jio_mart"

# File_Name=f"Walmart_VIJAYAWADA"

def email_alert_jio_mart_hubli():
    send_mail = False
    host = '192.168.100.215'
    port = '27017'
    db = 'jiomart'
    con = pymongo.MongoClient(f'mongodb://{host}:{port}/')
    mydb = con[db]
    conn = mydb[f"{File_Name}"]

    sql_con = mysql.connector.connect(host="192.168.100.215", user="root", password="xbyte",
                                      database="jio_mart_application")
    sql_cursor = sql_con.cursor()
    sql_cursor.execute('SELECT * FROM jio_mart_application.jio_mart_new_inputs_csv')
    records = sql_cursor.fetchall()
    input_sku = len(records)

    test = pd.DataFrame(list(conn.find()))
    if len(test) == input_sku:
        today_date = str(datetime.now().date())
        xlsx_path = fr'''\\192.168.100.249\DataGators\Temp\Ravi\Daily\Jio_mart_hubli\{datetime.now().strftime('%B')}\{today_date}'''
        if not os.path.exists(xlsx_path):
            os.makedirs(xlsx_path)
        test.pop('_id')
        test.insert(0, 'ID', range(1, len(test) + 1))
        # test.pop('Screenshot_Path')
        writer = pd.ExcelWriter(
            fr"{xlsx_path}\{File_Name}_data.xlsx",
            engine='xlsxwriter', options={'strings_to_urls': False})
        test.to_excel(writer, index=False)
        writer.close()
        print("Excel Generated")
        print(f"path - {xlsx_path}")
        #----------------------------------------------------------------
        today_date = str(datetime.now().date())
        today_path = fr'''\\192.168.100.249\DataGators\Temp\Ravi\Daily\Jio_mart_hubli\{datetime.now().strftime('%B')}\{today_date}'''
        if datetime.now().strftime('%A') == "Monday":
            previous_date = str(datetime.now().date() - timedelta(4))
        else:
            previous_date = str(datetime.now().date() - timedelta(1))
            # previous_date = str(datetime.now().date() - timedelta(6))
            # print(previous_date)
        current_time = datetime.now()
        if current_time.day == 1:
            try:
                temp_p_month = previous_date.split("-")[1]
                french_months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June',
                                 '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November',
                                 '12': 'December'}
                p_month = french_months[temp_p_month]
                print(p_month)
            except Exception as e:
                print(e)
            # temp_p_month = temp_p_month.repl

        else:
            p_month = datetime.now().strftime('%B')
        previous_date = str(datetime.now().date() - timedelta(1))
        # previous_path = fr'''\\192.168.100.249\DataGators\Temp\Ravi\Daily\Jio_mart_hubli\{datetime.now().strftime('%B')}\{previous_date}'''
        previous_path = fr'''\\192.168.100.249\DataGators\Temp\Ravi\Daily\Jio_mart_hubli\{(datetime.now()-timedelta(1)).strftime('%B')}\{previous_date}'''
        # previous_path = fr'''\\192.168.100.249\DataGators\Temp\Ravi\Daily\Jio_mart_hubli\March\{previous_date}'''
        # previous_path = fr'''\\192.168.100.249\DataGators\Temp\Ravi\Daily\Jio_mart_hubli\{(datetime.now()-timedelta(days=1)).strftime('%B')}\{previous_date}'''
        try:
            dbx = dropbox.Dropbox('Mw46Be7ueY4AAAAAAAAAAU00jILbPUEiwLeAT38dKe2r4RagMsmHZykPizAFE8VB')
            c_file_to = f'/Darshit/jiomart_jumbotail/Jio_mart_Hubli/Data/{datetime.now().strftime("%B")}/{File_Name}_data.xlsx'
            with open(fr'{xlsx_path}\{File_Name}_data.xlsx', 'rb')as f:
                dbx.files_upload(f.read(), c_file_to, mode=dropbox.files.WriteMode.overwrite)
                finalfileto1 = c_file_to
                result = dbx.sharing_create_shared_link_with_settings(finalfileto1)
                print("-> Dropbox Data Uploading Done")
        except Exception as e:
            print(e)
        # try:
        #     dbx2 = dropbox.Dropbox('Mw46Be7ueY4AAAAAAAAAAU00jILbPUEiwLeAT38dKe2r4RagMsmHZykPizAFE8VB')
        #     c_file_to2 = f'/Darshit/jiomart_jumbotail/Jio_mart_Hubli/Screenshots/{datetime.now().strftime("%B")}/{File_Name}_screenshots.zip'
        #     screenshot_path = fr'\\192.168.100.89\d\jiomart\{str(datetime.now().strftime("%d%m%Y"))}_screenshot'
        #     shutil.make_archive(screenshot_path, 'zip', screenshot_path)
        #     with open(fr'{screenshot_path}.zip', 'rb') as f:
        #         dbx2.files_upload(f.read(), c_file_to2, mode=dropbox.files.WriteMode.overwrite)
        #         finalfileto2 = c_file_to2
        #         result2 = dbx2.sharing_create_shared_link_with_settings(finalfileto2)
        #         print("-> Dropbox Screenshot Uploading Done")
        # except Exception as e:
        #     print(e)
        #--------------------------------------------------------------------------------------------
        try:
            today_file_name = f"{File_Name}_data.xlsx"
            today_file = pd.read_excel(today_path + '\\'+today_file_name)
            # today_file = today_file.astype('str')
            today_file_grp = today_file.groupby(['JPIN'])
            total_length = len(today_file.index)
            count = len(today_file_grp.size())
            dt = datetime.strptime(f'{previous_date}', '%Y-%m-%d').strftime('%Y-%m-%d')

            previous_file_name = f"{File_Name}_data.xlsx".replace(today_date,dt)
            previous_file = pd.read_excel(previous_path + '\\'+previous_file_name)
            previous_file_grp = previous_file.groupby(['JPIN'])
            # old_count = len(previous_file.index)
            old_count = len(previous_file_grp.size())
            # test =
            # print()
            today_file.columns = ['ID', 'JPIN', 'Product_Title', 'Category', 'Jiomart MRP',
                                  'Jio MOQ (Minimum Order Quantity)', 'MOQ From Title', 'Slab 1 MOQ',
                                  'Slab 1 Selling Price', 'Slab 1 Profit', 'Slab 2 MOQ', 'Slab 2 Selling Price',
                                  'Slab 2 Profit', 'Slab 3 MOQ', 'Slab 3 Selling Price', 'Slab 3 Profit',
                                  'Delivery Charges', 'Availability', 'Screenshots','Crawl Timestamp']
            previous_file.columns = ['ID', 'JPIN', 'Product_Title', 'Category', 'Jiomart MRP',
                                     'Jio MOQ (Minimum Order Quantity)', 'MOQ From Title', 'Slab 1 MOQ',
                                     'Slab 1 Selling Price', 'Slab 1 Profit', 'Slab 2 MOQ', 'Slab 2 Selling Price',
                                     'Slab 2 Profit', 'Slab 3 MOQ', 'Slab 3 Selling Price', 'Slab 3 Profit',
                                     'Delivery Charges', 'Availability', 'Screenshots','Crawl Timestamp']
            today_count = today_file.count(axis=0).to_dict()
            previous_count = previous_file.count(axis=0).to_dict()
            if today_count['Slab 1 Selling Price'] == today_count['Jiomart MRP'] and today_count['Screenshots'] == today_count['JPIN']:
                send_mail = True
            count_df = (pd.DataFrame.from_dict([today_count, previous_count])).T.fillna(0).astype(int)
            api_count = json.dumps(today_count)
            count_df.columns = ['count_new', 'count_old']
            all_columns = list(today_file.columns)
            # print(all_columns)
            # mandatory_column = ['crawl_date_time', 'site_name', 'review_url', 'country', 'amazon_url', 'asin', 'scrapingStatus', 'screenshotamazonpage', 'screenshotproductpage']
            today_file_str = today_file.astype('str')

            if send_mail:
                count_df_html = count_df.to_html(na_rep='0', justify='center', border=1).replace("<td>No</td>",
                                                                                                   '<td style="background-color:red;"><b>No</b></td>')
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 1))
                local_ip_address = s.getsockname()[0]

                emailId = "alerts@xbyte.io"
                emailpass = "wSsVR61/+hP5DKcszTH5Jbhpml9dVlL0HEV6iVSn7XSpTKzLoMdukkCdVlWjGPgfRDRpHDAWrLIhnBZShztYjdQszVtSDiiF9mqRe1U4J3x17qnvhDzPV2RdlhuAJYgIwwlqmWVoE88k+g=="

                send_to = [
                    'xbyte.qa@gmail.com',
                    'pi-xbyte@jumbotail.com',
                    'antony@jumbotail.com',
                    'komalp.xbyte@gmail.com',
                    'hariom.katheriya.xbyte@gmail.com',
                    'pb@jumbotail.com'

                ]
                cc = [


                ]
                bcc = [

                    'bhavesh.parekh.xbyte@gmail.com',
                    'ricky.jones@xbyte.io',
                    'tarun.xbyte@gmail.com',
                    'neelap.xbyte@gmail.com'
                    ]

                mail_content = list()
                mail_content.append("<html>")
                mail_content.append("<head>")
                mail_content.append("<style>")
                mail_content.append("table,th,td {border : 2px solid black;border-collapse: collapse;padding: 10px;}")
                mail_content.append("</style>")
                mail_content.append("</head>")
                mail_content.append("<body>")
                mail_content.append("<br><h3>Data Summary</h3>")
                mail_content.append("<table border='1'>")
                mail_content.append("<tr><td><b>File Name</b></td><td>" + str(today_file_name) + "</td></tr>")
                mail_content.append("<tr><td><b>Total Data</b></td><td>" + str(count) + "</td></tr>")
                mail_content.append("<tr><td><b>Previous Data</b></td><td>" + str(old_count) + "</td></tr>")
                mail_content.append("<tr><td><b>Dropbox Excel Link</b></td><td>" + str(result.url) + "</td></tr>")
                # mail_content.append("<tr><td><b>Dropbox Screenshots Link</b></td><td>" + str(result2.url) + "</td></tr>")
                # mail_content.append("<tr><td><b>File Validate</b></td><td>" + str(file_validate) + "</td></tr>")
                mail_content.append("</table>")
                mail_content.append("<br><h3>Data Count Comparision</h3>")
                m_content = json2html.convert(json=count_df_html)
                m_content = m_content.replace("&lt;", "<")
                m_content = m_content.replace("&gt;", ">")
                m_content = m_content.replace("\n", "")
                m_content = m_content.replace('&quot;', '"')
                mail_content.append(m_content)
                # mail_content.append("<br><h3>Row wise errors</h3>")
                mail_content.append("<table border='1'>")
                # mail_content.append("<tr><td><b>Price Missing for Stock_Status='1'</b></td><td>" + str(stock_status) + "</td></tr>")
                # mail_content.append("<tr><td><b>Price Missing Sold_by</b></td><td>" + str(sold_by) + "</td></tr>")
                # mail_content.append("<tr><td><b>crawl_date_time format issue</b></td><td>" + str(errordateformat) + "</td></tr>")
                mail_content.append("</table>")
                mail_content.append("</body>")
                mail_content.append("</html>")
                body = "".join(mail_content).replace("<td>No</td>",'<td style="background-color:red;"><b>No</b></td>')
                try:
                    # time.sleep()
                    msg = MIMEMultipart()
                    msg['From'] = emailId
                    msg['To'] = ",".join(send_to)
                    msg['CC'] = ",".join(cc)
                    msg['BCC'] = ",".join(bcc)
                    msg['Subject'] = f"[ALERT:120] JioMart Application Hubli (Date : " + str(datetime.now().date()) + ")"
                    msg.attach(MIMEText(body, 'html'))
                    s = smtplib.SMTP("smtp.zeptomail.com", 587)
                    s.starttls()
                    s.login(emailId, emailpass)
                    text = msg.as_string()
                    s.sendmail(emailId, send_to + cc + bcc, text)
                    print("Mail Sent ...")
                    s.quit()
                except Exception as e:
                    print(e)

                try:
                    import requests

                    url = "https://dev.xbytedev.co/count_dashboard/ajax.php?action=add_update_temp_taiga_project_count_data"

                    payload = {'project_id': '121',
                               'userstory_id': '1644',
                               'scraped': '1',
                               'delivered': '1',
                               'total_count': count,
                               'field_count': api_count}
                    files = [

                    ]
                    headers = {
                        'Cookie': 'PHPSESSID=khur8de2v4nrfa7a1cbhh7sqtd'
                    }

                    response = requests.request("POST", url, headers=headers, data=payload, files=files)

                    print(response.text)

                except Exception as e:
                    print("Error in Dashboard API Error Calling...", e)
            else:
                print('Check Internal Counts:', today_count)
        except Exception as e:
            print(e)
    else:
        print('Count does not match Input count.')
        os.system("hubli.bat")

if __name__ == '__main__':
    email_alert_jio_mart_hubli()