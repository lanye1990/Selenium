#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/20 10:48
# @Author : Lanye
# @Site : 
# @File : driver.py
# @Software: PyCharm

from selenium.webdriver import Remote
from selenium import webdriver

#定义浏览器驱动
def browser():
    host='http://127.0.0.1:4444/wd/hub'                       #定义运行主机的IP及端口号
    dc={"browserName": "chrome",                              #指定浏览器
        "version": "",
        "platform": "ANY",
        "javascriptEnabled": True,
        }
    driver = Remote(command_executor = host , desired_capabilities=dc)
    return driver

if __name__=='__main__':
    dr=browser()
    dr.get('http://www.baidu.com')
    #dr.quit()