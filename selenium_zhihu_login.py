# -*- coding: utf-8 -*-

from selenium import webdriver
# from scrapy.selector import Selector
import time


browser = webdriver.Chrome(executable_path='D:/chromedriver.exe')
browser.get("https://www.zhihu.com/signup?next=%2F")
time.sleep(5)
browser.find_element_by_xpath("//div[@class='SignContainer-switch']/span").click() # 第一次打开是注册页面然后模拟点击登陆按钮到达登陆界面
browser.find_element_by_xpath("//div[@class='SignFlow-accountInput Input-wrapper']/input[@name='username']").send_keys("username")
browser.find_element_by_xpath("//div[@class='Input-wrapper']/input[@name='password']").send_keys("password")
browser.find_element_by_xpath("//div[@class='Login-content']//button[@type='submit']").click()
print(browser.page_source) 
# t_selector = Selector(text=browser.page_source)
# result = t_selector.xpath("").extract()
browser.quit()
