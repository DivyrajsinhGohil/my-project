# import pandas as pd
# import re
#
# import dropbox
# import mysql.connector
# # import dropbox
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
# if __name__ == '__main__':
#
#     port_m = '27017'
#     host = 'localhost'
#     db = 'Jiomart_full_scrap'
#     con = pymongo.MongoClient(f'mongodb://{host}:{port_m}/')
#     mydb = con[db]
#     today_date_z = datetime.now().date()
#     var = f'jio_mart15_data'  # new table
#     conn = mydb[var]
#
#     counter = 1
#     #----change port number if you change server port
#     port = 4723
#     Appium_url = f"http://localhost:{port}/wd/hub"
#     desired_caps = {
#         "platformName": "Android",
#         "deviceName": "127.0.0.1:5565",
#         "appPackage": "com.jio.bapp",
#         "appActivity": "com.jio.bapp.activity.SplashActivity",
#         "noReset": "True",
#         "idleTimeout": 60000
#     }
#
#     driver = webdriver.Remote(Appium_url, desired_caps)
#     time.sleep(2)
#     WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "com.jio.bapp:id/search_src_text")))
#     print("wait Application is Loading")
#
#     click_search = driver.find_element_by_id('com.jio.bapp:id/search_src_text').click()
#     time.sleep(1)
#     records=['Red Bull 250 ml (Pack of 4)',
#     'Vicks VapoRub Pain Relief Balm 110 ml',
#     'Zandu Ultra Power Balm 25 ml',
#     'Zandu Pain Relief Balm 25 ml',
#     'Dabur Chatcola Hajmola 120 pcs',
#     'Pet Saffa Tablet 30 tablets',
#     'Durex Extra Ribbed Condoms 3 pcs',
#     'Lifree For Men & Women Adult Absorbent Pant (M, 24 - 33 inches) 10 count',
#     'Dabur Lal Tail 100 ml',
#     'MamyPoko Standard Pants (M) 1 count (7 - 12 kg)',
#     'Himani Cheetah Fast Pain Relief Ayurvedic Ointment 45 ml',
#     'Amrutanjan Maha Strong Pain Balm 8 ml',
#     'Moov Pain Relief Cream 50 g',
#     'Amrutanjan Extra Power Pain Balm 8 ml',
#     'Dabur Lemon Fizz Pudin Hara 5 g (Pack of 6)',
#     'Durex Extra Thin Condoms 3 pcs',
#     'Skore Shades Condoms 3 pcs',
#     'Himalaya Baby Lotion 100 ml',
#     'Johnson"s Baby Shampoo 100 ml',
#     'Himalaya Refreshing Baby Soap 75 g',
#     'Mothercare All We Know Baby Soap 75 g',
#     'Mothercare Basic Pants (L) 2 count (9 - 14 kg)',
#     'MamyPoko Extra Absorb Pants (XXL) 7 count (15 - 25 kg)',
#     'MamyPoko Extra Absorb Pants (L) 5 count (9 - 14 kg)',
#     'MamyPoko Extra Absorb Pants (M) 6 count (7- 12 kg)',
#     'Pampers Baby Dry Pants (M) 2 count (7 - 12 kg)',
#     ]
#     for k in records:
#         app_title = k
#         app_title = ' '.join(app_title.split()).strip()
#
#         print("---------- ----------------------------------------------------------------------------------------")
#         print("Product name ->", app_title)
#         # status=True
#         src_status = True
#         while src_status is True:
#             try:
#                 driver.find_element_by_id('com.jio.bapp:id/search_close_btn').click()
#             except:
#                 pass
#             try:
#                 send_keys = driver.find_element_by_id('com.jio.bapp:id/search_src_text').send_keys(app_title)
#             except:
#                 driver.find_element_by_id('com.jio.bapp:id/search_src_text').click()
#                 time.sleep(2)
#                 send_keys = driver.find_element_by_id('com.jio.bapp:id/search_src_text').send_keys(app_title)
#
#             try:
#                 send_keys.click()
#                 # driver.press_keycode(keycode=66)
#                 time.sleep(2)
#                 TouchAction(driver).tap(x=833, y=1310).perform()
#             except:
#                 TouchAction(driver).tap(x=833, y=1310).perform()
#             time.sleep(2)
#             # driver.press_keycode(keycode=66)
#             # time.sleep(4)
#             # -------------------------------------------------------------------------------------------------------
#             status = True
#             try:
#                 condition = driver.find_element_by_id('com.jio.bapp:id/tvCategory')
#             except:
#                 condition = ''
#             while condition != '' and status == True:
#                 click_search = driver.find_element_by_id('com.jio.bapp:id/search_src_text').click()
#                 time.sleep(2)
#                 send_keys = driver.find_element_by_id('com.jio.bapp:id/search_src_text').send_keys(app_title)
#                 try:
#                     send_keys.click()
#                     # driver.press_keycode(keycode=66)
#                     time.sleep(2)
#                     TouchAction(driver).tap(x=833, y=1310).perform()
#                 except:
#                     TouchAction(driver).tap(x=833, y=1310).perform()
#                 try:
#                     condition = driver.find_element_by_id('com.jio.bapp:id/tvCategory')
#                 except:
#                     condition = ''
#                 if condition == '':
#                     status = False
#
#             # -----------------------------------------------------------------------------------------------------------
#             WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH,
#                                                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")))
#
#             products_len = len(driver.find_elements_by_xpath(
#                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup'))
#
#             for num in range(1, products_len + 1):
#                 try:
#                     src_title = driver.find_element_by_xpath(
#                         f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]//android.widget.TextView[@resource-id="com.jio.bapp:id/tvProductName"]').text
#                     src_status = False
#                     if app_title == src_title:
#                         try:
#                             first_mrp = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]//android.widget.TextView[@resource-id="com.jio.bapp:id/mrp_txt"]').text
#                             first_mrp = re.findall('(\d+[.]*\d+)', first_mrp)[0]
#                         except Exception as e:
#                             first_mrp = ''
#
#                         try:
#                             moq = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]//android.widget.TextView[@resource-id="com.jio.bapp:id/pack_details_txt"]').text
#                         except Exception as e:
#                             moq = ''
#
#                         try:
#                             slab_1_moq = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.LinearLayout[1]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_quantity_txt"]').text
#                         except Exception as e:
#                             slab_1_moq = ""
#
#                         try:
#                             slab_2_moq = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.LinearLayout[1]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_quantity_txt"]').text
#                         except Exception as e:
#                             slab_2_moq = ""
#
#                         try:
#                             slab_3_moq = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[7]/android.widget.LinearLayout[1]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_quantity_txt"]').text
#                         except Exception as e:
#                             slab_3_moq = ""
#
#                         try:
#                             slab_1_price = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
#                             slab_1_price = re.findall('(\d+[.]*\d+)', slab_1_price)[0]
#                         except Exception as e:
#                             slab_1_price = ''
#
#                         try:
#                             slab_2_price = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
#                             slab_2_price = re.findall('(\d+[.]*\d+)', slab_2_price)[0]
#                         except Exception as e:
#                             slab_2_price = ''
#
#                         try:
#                             slab_3_price = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[7]/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
#                             slab_3_price = re.findall('(\d+[.]*\d+)', slab_3_price)[0]
#                         except Exception as e:
#                             slab_3_price = ''
#
#                         try:
#                             slab_1_profit = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.LinearLayout[3]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
#                         except Exception as e:
#                             slab_1_profit = ''
#
#                         try:
#                             slab_2_profit = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.LinearLayout[3]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
#                         except Exception as e:
#                             slab_2_profit = ''
#
#                         try:
#                             slab_3_profit = driver.find_element_by_xpath(
#                                 f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[7]/android.widget.LinearLayout[3]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
#                         except Exception as e:
#                             slab_3_profit = ''
#
#                         temp = {'Product_Title': src_title,
#                                 'Jiomart MRP': str(first_mrp),
#                                 'Jio MOQ (Minimum Order Quantity)': str(moq),
#                                 'MOQ From Title': '',
#                                 'Slab 1 MOQ': slab_1_moq, 'Slab 1 Selling Price': slab_1_price, 'Slab 1 Profit': slab_1_profit,
#                                 'Slab 2 MOQ': slab_2_moq,
#                                 "Slab 2 Selling Price": slab_2_price, 'Slab 2 Profit': slab_2_profit, 'Slab 3 MOQ': slab_3_moq,
#                                 "Slab 3 Selling Price": slab_3_price, 'Slab 3 Profit': slab_3_profit}
#
#
#                         # conn.create_index("JPIN", unique=True)
#                         conn.insert(temp)
#                         print("data inserted...", counter)
#                 except Exception as e:
#                     print(e)