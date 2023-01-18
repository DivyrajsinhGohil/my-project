# import re
# import hashlib
# import os
# import time
# from time import sleep
# from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
# import pymongo
# from datetime import datetime
#
# host = 'localhost'
# port_m = '27017'
# db = 'Jiomart_full_scrap'
# con = pymongo.MongoClient(f'mongodb://{host}:{port_m}/')
# mydb = con[db]
# today_date_z = datetime.now().date()
# var = f'{today_date_z}_data'
# conn = mydb[var]
# port =4726
# Appium_url = f"http://localhost:{port}/wd/hub"
# path = f'\\\\192.168.100.89\\d\\Jiomart_chennai_full_scrap\\{str(datetime.now().date())}_screenshot\\'
# if not os.path.exists(path):
#     os.makedirs(path)
# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "127.0.0.1:5565",
#     "appPackage": "com.jio.bapp",
#     "appActivity": "com.jio.bapp.activity.SplashActivity",
#     "noReset": "True",
#     "idleTimeout": 60000
# }
#
# driver = webdriver.Remote(Appium_url, desired_caps)
# touch = TouchAction(driver)
# time.sleep(5)
# print("-> Main page opened.")
# driver.swipe(472, 1489, 465, 1322)
# categories_len =len(driver.find_elements_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup"))
#
# for i in range(1,(categories_len+1)):
#     time.sleep(1)
#     category_name = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.LinearLayout/android.widget.TextView').text
#     print("category_name = ",category_name)
#     driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.LinearLayout').click()
#     time.sleep(2)
#     print("****** Ready for subcategory *****")
#     sub_category_names = []
#     sub_category_click_status = True
#     sub_category_names_done = []
#     while sub_category_click_status:
#         # sub_category_selector = driver.find_elements_by_xpath('//d.b.c.a.c')
#         sub_category_selector = driver.find_elements_by_xpath('//android.widget.LinearLayout')
#         for x in sub_category_selector:
#             name = x.get_attribute('content-desc')
#             if name not in sub_category_names and x is not None:
#                 sub_category_names.append(name)
#             else:
#                 pass
#         next_click_status = False
#         sub_category_names.remove(None)
#         for sub_category_name in sub_category_names:
#             if sub_category_name not in sub_category_names_done:
#                 next_click_status = True
#                 print(f"clicking on subcategory - {sub_category_name}")
#                 driver.find_element_by_xpath(f'//android.widget.LinearLayout[@content-desc="{sub_category_name}"]').click()
#                 time.sleep(2)
#                 swap_status=True
#                 products_list_done = []
#                 while swap_status:
#                     product_selector_len = len(driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup'))
#                     product_status = False
#                     for i in range(1,(product_selector_len+1)):
#                         try:
#                             while 1:
#                                 try:
#                                     product_name = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]//android.widget.TextView[@resource-id="com.jio.bapp:id/tvProductName"]').text
#                                     break
#                                 except:
#                                     i+=1
#                             if product_name not in products_list_done:
#                                 product_status = True
#                                 try:
#                                     product_price = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]//android.widget.TextView[@resource-id="com.jio.bapp:id/mrp_txt"]').text
#                                 except Exception as e:
#                                     product_price = ''
#                                 try:
#                                     jio_mart_price = ''
#                                 except Exception as e:
#                                     jio_mart_price = ''
#
#                                 try:
#                                     product_moq = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]//android.widget.TextView[@resource-id="com.jio.bapp:id/pack_details_txt"]').text
#                                 except Exception as e:
#                                     product_moq = ''
#                                 # try:
#                                 #     click_extra_btn = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]//android.widget.ImageView[@resource-id="com.jio.bapp:id/ivExpandScheme"]').click()
#                                 #     time.sleep(1)
#                                 # except Exception as e:
#                                 #     print(f"NO extra button available for product - {product_name}")
#
#                                 slab_1_moq = ''
#                                 try:
#                                     slab_1_moq = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.LinearLayout[1]/android.widget.TextView').text
#                                 except Exception as e:
#                                     slab_1_moq = ''
#                                 if not slab_1_moq:
#                                     continue
#                                 slab_2_moq = ''
#                                 try:
#                                     slab_2_moq = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.LinearLayout[1]/android.widget.TextView').text
#                                 except:
#                                     slab_2_moq = ''
#                                 slab_3_moq = ''
#                                 try:
#                                     slab_3_moq = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[7]/android.widget.LinearLayout[1]/android.widget.TextView').text
#                                 except:
#                                     slab_3_moq = ''
#                                 try:
#                                     slab_1_price =driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.LinearLayout[2]/android.widget.TextView').text
#                                 except:
#                                     slab_1_price = ''
#                                 try:
#                                     slab_2_price =driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.LinearLayout[2]/android.widget.TextView').text
#                                 except:
#                                     slab_2_price = ''
#                                 try:
#                                     slab_3_price =driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[7]/android.widget.LinearLayout[2]/android.widget.TextView').text
#                                 except:
#                                     slab_3_price = ''
#                                 try:
#                                     slab_1_profit = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.LinearLayout[3]/android.widget.TextView').text
#                                 except:
#                                     slab_1_profit = ''
#                                 try:
#                                     slab_2_profit = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.LinearLayout[3]/android.widget.TextView').text
#                                 except:
#                                     slab_2_profit = ''
#                                 try:
#                                     slab_3_profit = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{i}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[7]/android.widget.LinearLayout[3]/android.widget.TextView').text
#                                 except:
#                                     slab_3_profit = ''
#                                 product_hash_id = bytes(str(product_name),encoding='utf-8')
#                                 product_hash_id = int(hashlib.md5(product_hash_id).hexdigest(), 16) % (10 ** 8)
#                                 while True:
#                                     try:
#                                         driver.save_screenshot(path + str(product_hash_id) + ".png")
#                                         img_path = str(path + str(product_hash_id) + ".png")
#                                         break
#                                     except Exception as e:
#                                         print("screenshot Error ---- ",e)
#                                         sleep(1)
#                                 product_items = {'Product Id':product_hash_id,
#                                         'Product_Title': product_name,
#                                         'Category': category_name,
#                                         'Sub Category':sub_category_name,
#                                         'Product Price': str(product_price).replace('MRP', '').replace('Price ','').strip(),
#                                         'Jio Selling Price': jio_mart_price,
#                                         'Jio MOQ (Minimum Order Quantity)': str(product_moq).replace('MOQ : ', '').strip(),
#                                         'Slab 1 MOQ': slab_1_moq,
#                                         'Slab 1 Selling Price': slab_1_price,
#                                         'Slab 1 Profit':slab_1_profit,
#                                         'Slab 2 MOQ': slab_2_moq,
#                                         "Slab 2 Selling Price": slab_2_price,
#                                         'Slab 2 Profit':slab_2_profit,
#                                         'Slab 3 MOQ': slab_3_moq,
#                                         "Slab 3 Selling Price": slab_3_price,
#                                         'Slab 3 Profit': slab_3_profit,
#                                         'Availability': 'In Stock',
#                                         'Screenshot_Path': img_path}
#                                 try:
#                                     conn.create_index("Product Id", unique=True)
#                                     conn.insert_one(product_items)
#                                     print(f"Data inserted for product - {product_name}")
#                                 except Exception as e:
#                                     print(e)
#
#                                 products_list_done.append(product_name)
#                         except:
#                             pass
#                     if product_status:
#                         # driver.swipe(427, 1353, 427, 1097)
#                         # driver.swipe(443, 1316, 436, 1066)
#                         driver.swipe(369, 1431, 367, 349)
#                         time.sleep(2)
#                     else:
#                         swap_status = False
#                 sub_category_names_done.append(sub_category_name)
#             else:
#                 pass
#         if next_click_status:
#             pass
#         else:
#             sub_category_click_status = False
#     time.sleep(1)
#     print("<- Going to back")
#     driver.press_keycode(keycode=4)
#     time.sleep(5)
# print("--------------------------------------------------------------")
# smile_emoji = "\U0001f600"
# print(smile_emoji,smile_emoji,smile_emoji,"Yeah Full data Extraction finished.",smile_emoji,smile_emoji,smile_emoji)
# print("--------------------------------------------------------------")