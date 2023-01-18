# import re
#
# import dropbox
# import mysql.connector
# #import dropbox
# import pandas as pd
# import datetime
# import hashlib
# import os
# import time
# from time import sleep
# from appium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from appium.webdriver.common.touch_action import TouchAction
# import pymongo
# from datetime import datetime
#
# host = 'localhost'
# port_m = '27017'
# db = 'jiomart_chennai'
# con = pymongo.MongoClient(f'mongodb://{host}:{port_m}/')
# mydb = con[db]
# today_date_z = datetime.now().date()
# var = f'{today_date_z}_jio_mart'  # new table
# conn = mydb[var]
#
# counter = 1
# port =4723
# Appium_url = f"http://localhost:{port}/wd/hub"
# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "127.0.0.1:5555",
#     "appPackage": "com.jio.bapp",
#     "appActivity": "com.jio.bapp.activity.SplashActivity",
#     "noReset": "True",
#     "idleTimeout": 60000
# }
#
# def dropbox_linker(img_path, img):
#     try:
#         access_token = 'Mw46Be7ueY4AAAAAAAAAAU00jILbPUEiwLeAT38dKe2r4RagMsmHZykPizAFE8VB'
#         file_to = f'/Darshit/jiomart_jumbotail/Jio_mart_Chennai/Data/{datetime.now().strftime("%B")}/{datetime.now().date()}_jio_mart_screenshots'+'/'+img
#         dbx = dropbox.Dropbox(access_token)
#         with open(img_path, 'rb') as f:
#             dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
#         finalfileto1 = file_to
#         result = dbx.sharing_create_shared_link_with_settings(finalfileto1)
#         print("dropbox uploading done")
#         return result.url
#     except Exception as e:
#         print(e)
#         return re.findall("url='(.*?)'", str(e))[0]
# # ------------------------------------------------------main method ---------------------------------------------------
#
# if __name__ == '__main__':
#     os.system("adb disconnect 127.0.0.1:5555")
#     os.system("adb connect 127.0.0.1:5555")
#     sql_con = mysql.connector.connect(host="192.168.1.89", user="root", password="xbyte", database="jio_mart_chennai")
#     sql_cursor = sql_con.cursor()
#     sql_cursor.execute("select * from jio_mart_chennai.jio_mart_chennai_01_11_csv where status='pending'")#<-----------------------------------change here
#     records = sql_cursor.fetchall()
#
#     path = f'\\\\192.168.1.55\\d\\jiomart_screenshots\\{str(datetime.now().strftime("%d%m%Y"))}_screenshot\\'
#
#     if not os.path.exists(path):
#         os.makedirs(path)
#     driver = webdriver.Remote(Appium_url, desired_caps)
#     time.sleep(5)
#     WebDriverWait(driver, 60).until(
#         EC.presence_of_element_located((By.ID, "com.jio.bapp:id/search_src_text")))
#     print("wait")
#     click_search = driver.find_element_by_id('com.jio.bapp:id/search_src_text').click()
#     time.sleep(2)
#     # driver = webdriver.Remote(Appium_url, desired_caps)
#     # time.sleep(5)
#     # WebDriverWait(driver, 60).until(
#     #     EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@resource-id='com.jio.bapp:id/image']")))
#     # print("wait")
#
#     # click_banner = driver.find_element_by_xpath(
#     #     "//android.widget.ImageView[@resource-id='com.jio.bapp:id/image']").click()
#     # time.sleep(2)
#
#     for k in records:
#         title = k[2]
#         app_title = k[5]
#         title = ' '.join(title.split()).replace('!','').strip()
#         status_z = k[4]
#         print("--------------------------------------------------------------------------------------------------")
#         print("Product name ->",title)
#         if status_z == "no_data_found_2":#<-----------------------------------change here
#             pass
#         else:
#             src_status = True
#             while src_status is True:
#                 try:
#                     clear_src = driver.find_element_by_xpath(
#                         "//android.widget.ImageView[@resource-id='com.jio.bapp:id/search_close_btn']").click()
#                 except:
#                     pass
#                 find_search_btn = ''
#
#                 try:
#                     find_search_btn = driver.find_element_by_xpath(
#                         "//android.widget.EditText[@resource-id='com.jio.bapp:id/search_src_text']")
#                     find_search_btn.click()
#                     find_search_btn.send_keys(title)
#                     driver.press_keycode(keycode=66)
#                     # driver.implicitly_wait(30)
#                 except Exception as e:
#                     print(e)
#                     pass
#
#                 while True:
#                     try:
#                         WebDriverWait(driver, 60).until(EC.presence_of_element_located(
#                             (By.XPATH,
#                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")))
#                     except:
#                         time.sleep(2)
#                         # io_handle()
#                     try:
#                         length_frame = driver.find_elements_by_xpath(
#                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
#                         if length_frame != []:
#                             break
#                     except:
#                         time.sleep(2)
#
#                 # print(length_frame)
#
#                 for lf in range(1, len(length_frame) + 1):
#                     # driver.implicitly_wait(30)
#                     try:
#                         scr_name = driver.find_element_by_xpath(
#                             f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{lf}]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]").text
#                         src_status = False
#                         # ---------------------------------------------------------------#
#                         print(f"chechking match '{title}'=='{scr_name}'")
#                         if title.lower() in scr_name.lower():
#                             print("match found..............")
#                             # if ratio_number > 0.70:
#                             first_mrp = driver.find_element_by_xpath(
#                                 f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{lf}]//android.widget.TextView[@resource-id='com.jio.bapp:id/tvProductMrpPrice']").text
#                             snd_mrp = driver.find_element_by_xpath(
#                                 f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{lf}]//android.widget.TextView[@resource-id='com.jio.bapp:id/tvProductPrice']").text
#                             moq = driver.find_element_by_xpath(
#                                 f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{lf}]//android.widget.TextView[@resource-id='com.jio.bapp:id/tvProductMinOrder']").text
#                             try:
#                                 # click_extra_btn = driver.find_element_by_xpath(
#                                 #     "//android.widget.ImageView[@resource-id='com.jio.bapp:id/ivExpandScheme']").click()
#                                 click_extra_btn = driver.find_element_by_xpath(
#                                     f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{lf}]/android.widget.FrameLayout//android.widget.ImageView[@resource-id='com.jio.bapp:id/ivExpandScheme']").click()
#                                 time.sleep(2)
#                             except Exception as e:
#                                 print(e, "NO extra button available")
#                             # length_of_dropdown = driver.find_elements_by_xpath(
#                             #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout")
#                             try:
#                                 # driver.implicitly_wait(30)
#                                 slab_1_moq = driver.find_element_by_xpath(
#                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView').text
#                                 slab_1_moq = re.findall('Buy(.*?)at', slab_1_moq)[0].strip()
#                             except Exception as e:
#                                 print(e)
#                                 slab_1_moq = ''
#
#                             try:
#                                 slab_2_moq = driver.find_element_by_xpath(
#                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView').text
#                                 slab_2_moq = re.findall('Buy(.*?)at', slab_2_moq)[0].strip()
#                             except:
#                                 slab_2_moq = ''
#                             try:
#                                 slab_3_moq = driver.find_element_by_xpath(
#                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView').text
#                                 slab_3_moq = re.findall('Buy(.*?)at', slab_3_moq)[0].strip()
#                             except:
#                                 slab_3_moq = ''
#                             try:
#                                 slab_1_price = driver.find_element_by_xpath(
#                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView').text
#                                 slab_1_price = re.findall('Rs.(.*?)each', slab_1_price)[0].strip()
#                             except:
#                                 slab_1_price = ''
#                             try:
#                                 slab_2_price = driver.find_element_by_xpath(
#                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.TextView').text
#                                 slab_2_price = re.findall('Rs.(.*?)each', slab_2_price)[0].strip()
#                             except:
#                                 slab_2_price = ''
#                             try:
#                                 slab_3_price = driver.find_element_by_xpath(
#                                     '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.TextView').text
#                                 slab_3_price = re.findall('Rs.(.*?)each', slab_3_price)[0].strip()
#                             except:
#                                 slab_3_price = ''
#                             while True:
#                                 temp_time = str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
#                                 try:
#                                     driver.save_screenshot(
#                                         path + f'{k[1]}_{temp_time}' + ".png")
#                                     img_path = str(
#                                         path + f'{k[1]}_{temp_time}' + ".png")
#                                     dropbox_link = dropbox_linker(img_path=img_path, img=img_path.split("\\")[-1])
#                                     break
#                                 except Exception as e:
#                                     print(e)
#                                     sleep(2)
#
#                             temp = {'JPIN': k[1], 'Product_Title': scr_name, 'Category': k[3],
#                                     'Jiomart': str(first_mrp).replace('MRP', '').replace('Price', '').strip(),
#                                     'Jio MOQ (Minimum Order Quantity)': str(moq).replace('MOQ : ', '').strip(),
#                                     'Jio Selling Price': snd_mrp,
#                                     'MOQ From Title': '',
#                                     'Slab 1 MOQ': slab_1_moq, 'Slab 1 Selling Price': slab_1_price,
#                                     'Slab 2 MOQ': slab_2_moq,
#                                     "Slab 2 Selling Price": slab_2_price, 'Slab 3 MOQ': slab_3_moq,
#                                     "Slab 3 Selling Price": slab_3_price, 'Delivery Charges': '',
#                                     'Availability': 'In Stock',
#                                     'Screenshots':dropbox_link}
#                             try:
#                                 conn.create_index("JPIN", unique=True)
#                                 conn.insert(temp)
#                                 print("data inserted...", counter)
#                                 try:
#                                     sql_cursor.execute(
#                                         f"update jio_mart_chennai.jio_mart_chennai_01_11_csv set status = 'done' where jpin = '{k[1]}'")
#                                     sql_con.commit()
#                                     print("sql status updated - ", k[1])
#                                 except Exception as e:
#                                     print(e, "error in update status in sql -", k[1])
#                                 counter += 1
#                             except Exception as e:
#                                 print(e)
#                             print(
#                                 "--------------------------------------------------------------------------------------------------")
#                             break
#                     except:
#                         print("------------------------------src name not found ------------------------------")
#                         continue
#                 else:
#                     print("***********************************************************************************************")
#                     print("Product NOt found -> jpin = ",k[1])
#                     while True:
#                         temp_time = str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
#                         try:
#                             driver.save_screenshot(
#                                 path + f'{k[1]}_{temp_time}' + ".png")
#                             img_path = str(
#                                 path + f'{k[1]}_{temp_time}' + ".png")
#                             dropbox_link = dropbox_linker(img_path=img_path, img=img_path.split("\\")[-1])
#                             break
#                         except Exception as e:
#                             print(e)
#                             sleep(2)
#                     temp = {'JPIN': k[1], 'Product_Title': title, 'Category': k[3],
#                             'Jiomart': '', 'Jio MOQ (Minimum Order Quantity)': '', 'Jio Selling Price': '',
#                             'MOQ From Title': '',
#                             'Slab 1 MOQ': '', 'Slab 1 Selling Price': '', 'Slab 2 MOQ': '',
#                             "Slab 2 Selling Price": '', 'Slab 3 MOQ': '',
#                             "Slab 3 Selling Price": '', 'Delivery Charges': '',
#                             'Availability': 'Product Not Available',
#                             'Screenshots':dropbox_link}
#                     try:
#                         conn.create_index("JPIN", unique=True)
#                         conn.insert(temp)
#                         print("data inserted...", counter)
#                         try:
#                             sql_cursor.execute(
#                                 f"update jio_mart_chennai.jio_mart_chennai_01_11_csv set status = 'not found' where jpin = '{k[1]}'")
#                             sql_con.commit()
#                             print("sql status updated no found - ", k[1])
#                         except Exception as e:
#                             print(e, "error in update status in sql -", k[1])
#                         counter += 1
#                     except Exception as e:
#                         print(e)
#                     print("***********************************************************************************************")
#
#
#
