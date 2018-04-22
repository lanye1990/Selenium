#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/20 10:50
# @Author : Lanye
# @Site : 
# @File : prtscr.py.py
# @Software: PyCharm

from selenium import webdriver
import os

def screenShot(driver,file_name):

    ###获取测试用例目录
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir=str(base_dir)
    base_dir=base_dir.replace("\\","/")

    ###截屏
    base=base_dir.split('/test_case')[0]
    file_path=base+'/report/image/'+file_name
    driver.get_screenshot_as_file(file_path)

if __name__=='__main__':
    driver = webdriver.Firefox();
    driver.get("https://www.baidu.com")
    screenShot(driver,'baidu.jpg')
    driver.quit()
