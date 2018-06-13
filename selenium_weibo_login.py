# -*- coding: utf-8 -*-

from selenium import webdriver
# from scrapy.selector import Selector
import time


browser = webdriver.Chrome(executable_path='D:/chromedriver.exe')
browser.get("https://weibo.com")
# 等待浏览器加载完成
time.sleep(20)

browser.find_element_by_xpath("//div[@node-type='username_box']/div[@class='input_wrap']/input[@name='username']").send_keys("username")
browser.find_element_by_xpath("//div[@node-type='password_box']/div[@class='input_wrap']/input[@name='password']").send_keys("password")
browser.find_element_by_xpath("//div[@class='info_list login_btn']/a").click()
print(browser.page_source)
# t_selector = Selector(text=browser.page_source)
# result = t_selector.xpath("").extract()
browser.quit()
