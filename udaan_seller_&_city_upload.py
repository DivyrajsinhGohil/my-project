import datetime
import os
import re
import pymongo
import pandas as pd
import dropbox

today = datetime.datetime.today()
date = today.strftime('%Y_%m_%d')


def seller_excel():
    conn = pymongo.MongoClient('192.168.100.68', 27017)
    mydb = conn["Udaan_sellar_daily"]
    mycol = mydb[f'Udaan_sellar_data_{date}']
    myquery = {}
    cursor = mycol.find(myquery)
    df = pd.DataFrame(cursor)
    df.pop('_id')
    path = f"\\\\192.168.100.249\\DataGators\\Temp\\Ravi\\Udaan_Seller\\Udaan_once_off_{date}\\"
    if not os.path.exists(path):
        os.makedirs(path)
    writer = pd.ExcelWriter(path + f'Udaan_sellar_data_{date}.xlsx', engine='xlsxwriter',
                            options={'strings_to_urls': False})
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    print('Seller file generated at:-', path)


def city_excel():
    conn = pymongo.MongoClient('192.168.100.241', 27017)
    mydb = conn["Udaan_City_daily"]
    mycol = mydb[f'Udaan_City_data_{date}']
    myquery = {}
    cursor = mycol.find(myquery)
    df = pd.DataFrame(cursor)
    df.pop('_id')
    path = f"\\\\192.168.100.249\\DataGators\\Temp\\Ravi\\Udaan_city\\Udaan_once_off_{date}\\"
    # path = f"E:\\sagar\\Udaan_city\\Udaan_once_off_{date}\\"

    if not os.path.exists(path):
        os.makedirs(path)
    writer = pd.ExcelWriter(path + f'Udaan_City_data_{date}.xlsx', engine='xlsxwriter',
                            options={'strings_to_urls': False})
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    print('City file generated at:-', path)


def seller_data():
    path = fr'\\192.168.100.249\DataGators\Temp\Ravi\Udaan_Seller\Udaan_once_off_{date}'
    File_Name = f'Udaan_sellar_data_{date}.xlsx'
    try:
        dbx = dropbox.Dropbox('Mw46Be7ueY4AAAAAAAAAAU00jILbPUEiwLeAT38dKe2r4RagMsmHZykPizAFE8VB')
        # c_file_to = f'/Darshit/Jio_mart_ganga/Data/{File_Name}'
        c_file_to = f'/Sagar/Udaan_seller/{File_Name}'

        with open(fr'{path}\{File_Name}', 'rb') as f:
            dbx.files_upload(f.read(), c_file_to, mode=dropbox.files.WriteMode.overwrite)
            finalfileto1 = c_file_to
            result = dbx.sharing_create_shared_link_with_settings(finalfileto1)
        file_link = result.url
        print("-> Dropbox Data Uploading Done")
    except Exception as e:
        print(e)
        file_link = re.findall("url='(.*?)'", str(e))[0]
    print(file_link)


def city_data():
    path = fr'\\192.168.100.249\DataGators\Temp\Ravi\Udaan_city\Udaan_once_off_{date}'
    File_Name = f'Udaan_city_data_{date}.xlsx'
    try:
        dbx = dropbox.Dropbox('Mw46Be7ueY4AAAAAAAAAAU00jILbPUEiwLeAT38dKe2r4RagMsmHZykPizAFE8VB')
        # c_file_to = f'/Darshit/Jio_mart_ganga/Data/{File_Name}'
        c_file_to = f'/Sagar/Udaan_city/{File_Name}'
        with open(fr'{path}\{File_Name}', 'rb') as f:
            dbx.files_upload(f.read(), c_file_to, mode=dropbox.files.WriteMode.overwrite)
            finalfileto1 = c_file_to
            result = dbx.sharing_create_shared_link_with_settings(finalfileto1)
            file_link = result.url
        print("-> Dropbox Data Uploading Done")
    except Exception as e:
        print(e)
        file_link = re.findall("url='(.*?)'", str(e))[0]
    print(file_link)

def seller_excel_9am():
    conn = pymongo.MongoClient('192.168.100.68', 27017)
    mydb = conn["Udaan_sellar_daily_9AM"]
    mycol = mydb[f'Udaan_sellar_data_{date}']
    myquery = {}
    cursor = mycol.find(myquery)
    df = pd.DataFrame(cursor)
    df.pop('_id')
    path = f"\\\\192.168.100.249\\DataGators\\Temp\\Ravi\\Udaan_Seller_9am\\Udaan_once_off_{date}\\"
    if not os.path.exists(path):
        os.makedirs(path)
    writer = pd.ExcelWriter(path + f'Udaan_sellar_data_{date}.xlsx', engine='xlsxwriter',
                            options={'strings_to_urls': False})
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    print('Seller file generated at:-', path)


def city_excel_9am():
    conn = pymongo.MongoClient('192.168.100.241', 27017)
    mydb = conn["Udaan_City_daily_9AM"]
    mycol = mydb[f'Udaan_City_data_{date}']
    myquery = {}
    cursor = mycol.find(myquery)
    df = pd.DataFrame(cursor)
    df.pop('_id')
    path = f"\\\\192.168.100.249\\DataGators\\Temp\\Ravi\\Udaan_city_9am\\Udaan_once_off_{date}\\"
    # path = f"E:\\sagar\\Udaan_city\\Udaan_once_off_{date}\\"

    if not os.path.exists(path):
        os.makedirs(path)
    writer = pd.ExcelWriter(path + f'Udaan_City_data_{date}.xlsx', engine='xlsxwriter',
                            options={'strings_to_urls': False})
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    print('City file generated at:-', path)


def seller_data_9am():
    path = fr'\\192.168.100.249\DataGators\Temp\Ravi\Udaan_Seller_9am\Udaan_once_off_{date}'
    File_Name = f'Udaan_sellar_data_{date}.xlsx'
    try:
        dbx = dropbox.Dropbox('Mw46Be7ueY4AAAAAAAAAAU00jILbPUEiwLeAT38dKe2r4RagMsmHZykPizAFE8VB')
        # c_file_to = f'/Darshit/Jio_mart_ganga/Data/{File_Name}'
        c_file_to = f'/Sagar/Udaan_seller_9AM/{File_Name}'

        with open(fr'{path}\{File_Name}', 'rb') as f:
            dbx.files_upload(f.read(), c_file_to, mode=dropbox.files.WriteMode.overwrite)
            finalfileto1 = c_file_to
            result = dbx.sharing_create_shared_link_with_settings(finalfileto1)
        file_link = result.url
        print("-> Dropbox Data Uploading Done")
    except Exception as e:
        print(e)
        file_link = re.findall("url='(.*?)'", str(e))[0]
    print(file_link)


def city_data_9am():
    path = fr'\\192.168.100.249\DataGators\Temp\Ravi\Udaan_city_9am\Udaan_once_off_{date}'
    File_Name = f'Udaan_city_data_{date}.xlsx'
    try:
        dbx = dropbox.Dropbox('Mw46Be7ueY4AAAAAAAAAAU00jILbPUEiwLeAT38dKe2r4RagMsmHZykPizAFE8VB')
        # c_file_to = f'/Darshit/Jio_mart_ganga/Data/{File_Name}'
        c_file_to = f'/Sagar/Udaan_city_9AM/{File_Name}'
        with open(fr'{path}\{File_Name}', 'rb') as f:
            dbx.files_upload(f.read(), c_file_to, mode=dropbox.files.WriteMode.overwrite)
            finalfileto1 = c_file_to
            result = dbx.sharing_create_shared_link_with_settings(finalfileto1)
            file_link = result.url
        print("-> Dropbox Data Uploading Done")
    except Exception as e:
        print(e)
        file_link = re.findall("url='(.*?)'", str(e))[0]
    print(file_link)

if __name__ == '__main__':
    # city_excel()
    # seller_excel()
    city_data()
    # seller_data()
    # city_excel_9am()
    # seller_excel_9am()
    # city_data_9am()
    # seller_data_9am()
