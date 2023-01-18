# import time
#
# import scrapy
# import os
# import selenium
# from scrapy.cmdline import execute
# from scrapy.http import HtmlResponse
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# if __name__ == '__main__':
#
# # class Demo1Spider(scrapy.Spider):
# #     name = 'demo1'
# #     allowed_domains = ['demo1.com']
# #     start_urls = ['https://example.com']
# #
# #     def parse(self, response):
# DRIVER_PATH = r'D:\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# # driver.get('https://www.flipkart.com/')
# try:
#     driver.get(
#         'https://www.google.co.in/maps/search/Petrol+pump/@28.6885191,77.1041781,15z/data=!3m1!4b1!4m7!2m6!3m5!1sPetrol+pump!2s28.68852,77.112965!4m2!1d77.112965!2d28.68852')
#     div_sel = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[4]/div[1]')
#     for i in range(0,5):
#         driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", div_sel)
#     print("done")
# except Exception as e:
#     print(e)
