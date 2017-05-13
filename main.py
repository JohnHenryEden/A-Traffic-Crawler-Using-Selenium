# coding=utf-8
from selenium import webdriver
import urllib.request
import string
import os
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.nitrafficindex.com/")
driver.switch_to.default_content()
frame = driver.find_element_by_id('mainIframe')
driver.switch_to.frame(frame)
driver.find_element_by_link_text("道路实时交通指数").click()
time.sleep(2)
#driver.switch_to.default_content()
#frame1 = driver.find_element_by_id('mainIframe')
#driver.switch_to.frame(frame1)0
driver.find_elements_by_class_name("combo-arrow")[2].click()
driver.find_elements_by_xpath("//div[@value='440100']")[2].click()  # #绝了
# driver.find_element_by_xpath("//option[@value='50']")
time.sleep(2)
stuckClass = driver.find_elements_by_class_name("datagrid-row")
data = open("Today's Traffic Report.txt", "w")
data.write("=================================\n数据说明如下：\n  道路名称\n  道路起点\n  道路终点\n  交通指数（越高说明越堵）\n  平均速度\n  道路等级\n  拥堵等级（请无视，没有用的）\n=================================\n")
#todo: loop until all roads were grabbed
countdown = 50
while (stuckClass):
    for rowNumber in range(0, 9):
        try:
            data.write(driver.find_element_by_id("datagrid-row-r6-2-%d" % rowNumber).text)
            data.write('\n')
            data.write('\n')
        except:
            print("Skipped page due to some error.")
            countdown -= 1
            if (countdown == 0):
                exit()
    time.sleep(2)
    driver.find_element_by_class_name("pagination-next").click()
#for i in range(0, stuckClass.__len__()):
#    data.write(stuckClass[i].find_element_by_class_name("").text)
#todo: set grab frequency
