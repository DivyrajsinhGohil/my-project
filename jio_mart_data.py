import re
import dropbox
import mysql.connector
import datetime
import os
import time
from time import sleep
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import pymongo
from datetime import datetime

# '--port', f'{port}'


host = 'localhost'
port_m = '27017'
db = 'jiomart_chennai'
con = pymongo.MongoClient(f'mongodb://{host}:{port_m}/')
mydb = con[db]
today_date_z = datetime.now().date()
var = f'{today_date_z}_jio_mart'  # new table
conn = mydb[var]

counter = 1
#----change port number if you change server port
port = 4727
Appium_url = f"http://localhost:{port}/wd/hub"
desired_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:5565",
    "appPackage": "com.jio.bapp",
    "appActivity": "com.jio.bapp.activity.SplashActivity",
    "noReset": "True",
    "idleTimeout": 60000
}

def dropbox_linker(img_path, img):
    try:
        access_token = 'Mw46Be7ueY4AAAAAAAAAAU00jILbPUEiwLeAT38dKe2r4RagMsmHZykPizAFE8VB'
        file_to = f'/Darshit/jiomart_jumbotail/Jio_mart_Chennai/Data/{datetime.now().strftime("%B")}/{datetime.now().date()}_jio_mart_screenshots'+'/'+img
        # file_to = f'/Bhargav/jiomart_jumbotail/Jio_mart_Chennai/Data/{datetime.now().strftime("%B")}/{datetime.now().date()}_jio_mart_screenshots'+'/'+img
        dbx = dropbox.Dropbox(access_token)
        with open(img_path, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        finalfileto1 = file_to
        result = dbx.sharing_create_shared_link_with_settings(finalfileto1)
        print("dropbox uploading done")
        return result.url
    except Exception as e:
        print(e)
        return re.findall("url='(.*?)'", str(e))[0]
# ------------------------------------------------------main method ---------------------------------------------------

# os.system("python bluestack_run.py")
os.system("adb disconnect 127.0.0.1:5565")
os.system("adb connect 127.0.0.1:5565")
# appium_service = AppiumService() # <-- For KVM
# appium_service.start(args=['--base-path', '/wd/hub'])
# appium_service.start(args=['--base-path', '/wd/hub', '--port', f'{port}'])
sql_con = mysql.connector.connect(host="192.168.100.55", user="root", password="xbyte", database="jio_mart_chennai")
sql_cursor = sql_con.cursor()
sql_cursor.execute("select * from jio_mart_chennai_01_11_csv where status='pending'")#<-----------------------------------change here
records = sql_cursor.fetchall()
path = f'\\\\192.168.100.55\\d\\jiomart_screenshots\\{str(datetime.now().strftime("%d%m%Y"))}_screenshot\\'
print("total count = ",len(records))


if not os.path.exists(path):
    os.makedirs(path)
driver = webdriver.Remote(Appium_url, desired_caps)
time.sleep(2)
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "com.jio.bapp:id/search_src_text")))
print("wait Application is Loading")

click_search = driver.find_element_by_id('com.jio.bapp:id/search_src_text').click()
time.sleep(1)

for k in records:
    title = k[2]
    app_title = k[5]
    app_title = ' '.join(app_title.split()).strip()

    print("---------- ----------------------------------------------------------------------------------------")
    print("Product name ->", app_title)
    # status=True
    src_status = True
    while src_status is True:
        try:
            driver.find_element_by_id('com.jio.bapp:id/search_close_btn').click()
        except:
            pass
        try:
            send_keys = driver.find_element_by_id('com.jio.bapp:id/search_src_text').send_keys(app_title)
        except:
            driver.find_element_by_id('com.jio.bapp:id/search_src_text').click()
            time.sleep(2)
            send_keys = driver.find_element_by_id('com.jio.bapp:id/search_src_text').send_keys(app_title)

        try:
            send_keys.click()
            # driver.press_keycode(keycode=66)
            time.sleep(2)
            TouchAction(driver).tap(x=833, y=1310).perform()
        except:
            TouchAction(driver).tap(x=833, y=1310).perform()
        time.sleep(2)
        # driver.press_keycode(keycode=66)
        # time.sleep(4)
        # -------------------------------------------------------------------------------------------------------
        status=True
        try:
            condition = driver.find_element_by_id('com.jio.bapp:id/tvCategory')
        except:
            condition = ''
        while condition!='' and status==True:
            click_search = driver.find_element_by_id('com.jio.bapp:id/search_src_text').click()
            time.sleep(2)
            send_keys = driver.find_element_by_id('com.jio.bapp:id/search_src_text').send_keys(app_title)
            try:
                send_keys.click()
                # driver.press_keycode(keycode=66)
                time.sleep(2)
                TouchAction(driver).tap(x=833, y=1310).perform()
            except:
                TouchAction(driver).tap(x=833, y=1310).perform()
            try:
                condition = driver.find_element_by_id('com.jio.bapp:id/tvCategory')
            except:
                condition = ''
            if condition=='':
                status=False

        # -----------------------------------------------------------------------------------------------------------
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")))

        products_len = len(driver.find_elements_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup'))

        for num in range(1,products_len+1):
            try:
                src_title = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]//android.widget.TextView[@resource-id="com.jio.bapp:id/tvProductName"]').text
                src_status = False
                if app_title==src_title:
                    try:
                        first_mrp=driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]//android.widget.TextView[@resource-id="com.jio.bapp:id/mrp_txt"]').text
                        first_mrp=re.findall('(\d+[.]*\d+)',first_mrp)[0]
                    except Exception as e:
                        first_mrp = ''

                    try:
                        moq = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]//android.widget.TextView[@resource-id="com.jio.bapp:id/pack_details_txt"]').text
                    except Exception as e:
                        moq = ''

                    try:
                        slab_1_moq = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.LinearLayout[1]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_quantity_txt"]').text
                        if slab_1_moq:
                            slab_1_flag=True
                            if '-' in slab_1_moq:
                                moq=slab_1_moq.split('-')[-1]
                            else:
                                moq=slab_1_moq
                    except Exception as e:
                        slab_1_moq=""


                    try:
                        slab_2_moq = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.LinearLayout[1]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_quantity_txt"]').text
                    except Exception as e:
                        slab_2_moq=""

                    try:
                        slab_3_moq = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[7]/android.widget.LinearLayout[1]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_quantity_txt"]').text
                    except Exception as e:
                        slab_3_moq=""

                    try:
                        slab_1_price = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
                        slab_1_price = re.findall('(\d+[.]*\d+)', slab_1_price)[0]
                        if slab_1_flag and slab_1_price:
                            jiomart_SP=slab_1_price
                    except Exception as e:
                        slab_1_price=''

                    try:
                        slab_2_price = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
                        slab_2_price = re.findall('(\d+[.]*\d+)', slab_2_price)[0]
                    except Exception as e:
                        slab_2_price=''

                    try:
                        slab_3_price = driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[7]/android.widget.LinearLayout[2]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
                        slab_3_price = re.findall('(\d+[.]*\d+)', slab_3_price)[0]
                    except Exception as e:
                        slab_3_price=''

                    try:
                        slab_1_profit=driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[3]/android.widget.LinearLayout[3]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
                    except Exception as e:
                        slab_1_profit =''

                    try:
                        slab_2_profit=driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[5]/android.widget.LinearLayout[3]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
                    except Exception as e:
                        slab_2_profit =''

                    try:
                        slab_3_profit=driver.find_element_by_xpath(f'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[{num}]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TableLayout/android.widget.TableRow[7]/android.widget.LinearLayout[3]//android.widget.TextView[@resource-id="com.jio.bapp:id/moq_price_txt"]').text
                    except Exception as e:
                        slab_3_profit =''

                    while True:
                        temp_time = str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
                        try:
                            driver.save_screenshot(
                                path + f'{k[1]}_{temp_time}' + ".png")
                            img_path = str(
                                path + f'{k[1]}_{temp_time}' + ".png")
                            dropbox_link = dropbox_linker(img_path=img_path, img=img_path.split("\\")[-1])
                            # dropbox_link=""
                            break
                        except Exception as e:
                            print(e)
                            sleep(2)

                    temp = {'JPIN':k[1], 'Product_Title': src_title, 'Category': k[3],
                            'Jiomart MRP': str(first_mrp),
                            'Jiomart SP': str(jiomart_SP),
                            'Jio MOQ (Minimum Order Quantity)': str(moq),
                            'MOQ From Title': '',
                            'Slab 1 MOQ': slab_1_moq, 'Slab 1 Selling Price': slab_1_price,'Slab 1 Profit':slab_1_profit,
                            'Slab 2 MOQ': slab_2_moq,
                            "Slab 2 Selling Price": slab_2_price, 'Slab 2 Profit':slab_2_profit,'Slab 3 MOQ': slab_3_moq,
                            "Slab 3 Selling Price": slab_3_price, 'Slab 3 Profit':slab_3_profit,'Delivery Charges': '',
                            'Availability': 'In Stock',
                            'Screenshots': dropbox_link}
                    try:
                        temp['Crawl Timestamp'] = datetime.strftime(datetime.now(),
                                                                             '%d/%m/%Y %H:%M:%S')
                    except Exception as e:
                        print("Error in Date of scrape", e)

                    try:
                        conn.create_index("JPIN", unique=True)
                        conn.insert(temp)
                        print("data inserted...", counter)
                        try:
                            sql_cursor.execute(
                                f"update jio_mart_chennai.jio_mart_chennai_01_11_csv set status = 'done' where jpin = '{k[1]}'")
                            sql_con.commit()
                            print("sql status updated - ", k[1])
                        except Exception as e:
                            print(e, "error in update status in sql -", k[1])
                        counter += 1
                    except Exception as e:
                        print(e)
                    print("--------------------------------------------------------------------------------------------------")
                    break
            except:
                print("------------------------------src name not found ------------------------------")
                continue
        else:
            while True:
                temp_time = str(datetime.now().strftime("%d-%m-%Y_%H-%M-%S"))
                try:
                    driver.save_screenshot(
                        path + f'{k[1]}_{temp_time}' + ".png")
                    img_path = str(
                        path + f'{k[1]}_{temp_time}' + ".png")
                    dropbox_link = dropbox_linker(img_path=img_path, img=img_path.split("\\")[-1])

                    #dropbox_link=""
                    break
                except Exception as e:
                    print(e)
                    sleep(2)
            temp = {'JPIN': k[1], 'Product_Title':title , 'Category': k[3],
                    'Jiomart MRP': '',
                    'Jiomart SP': '',
                    'Jio MOQ (Minimum Order Quantity)': '',
                    'MOQ From Title': '',
                    'Slab 1 MOQ': '', 'Slab 1 Selling Price': '', 'Slab 1 Profit':'',
                    'Slab 2 MOQ': '',
                    "Slab 2 Selling Price":'', 'Slab 2 Profit':'', 'Slab 3 MOQ': '',
                    "Slab 3 Selling Price": '', 'Slab 3 Profit':'', 'Delivery Charges': '',
                    'Availability': 'Product Not Available',
                    'Screenshots': dropbox_link}
            try:
                temp['Crawl Timestamp'] = datetime.strftime(datetime.now(),
                                                            '%d/%m/%Y %H:%M:%S')
            except Exception as e:
                print("Error in Date of scrape", e)

            try:
                conn.create_index("JPIN", unique=True)
                conn.insert(temp)
                print("data inserted...", counter)
                try:
                    sql_cursor.execute(
                        f"update jio_mart_chennai.jio_mart_chennai_01_11_csv set status = 'not found' where jpin = '{k[1]}'")
                    sql_con.commit()
                    print("sql status updated no found - ", k[1])
                except Exception as e:
                    print(e, "error in update status in sql -", k[1])
                counter += 1
            except Exception as e:
                print(e)
            print("***********************************************************************************************")
os.system("python gen_jio_mart_csv.py")
# exec(open("gen_jio_mart_csv.py").read())



