#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/20 10:49
# @Author : Lanye
# @Site : 
# @File : public.py
# @Software: PyCharm


from selenium import webdriver
#from test_wjpublic import openConfgXml

#tapath = openConfgXml.GetTestdatapath()


def setUp(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    options.add_argument('disable-infobars')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("–incognito")
    options.add_argument("--disable-plugins")
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False,
             "download.default_directory": tapath}
    options.add_experimental_option("prefs", prefs)
    self.driver = webdriver.Chrome(chrome_options=options)
    self.driver.implicitly_wait(30)
    openConfgXml.GetUrl(self)


def setUpOptions(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    options.add_argument('disable-infobars')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("–incognito")
    options.add_argument("--disable-plugins")
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False,
             "download.default_directory": tapath}
    options.add_experimental_option("prefs", prefs)

    return options

    # self.driver = webdriver.Chrome(chrome_options=options)
    # self.driver.implicitly_wait(30)
    # openConfgXml.GetUrl(self)


def tearDown(self):
    self.driver.quit()


def close_otherWindow(self):
    # 关闭除了当前窗口外的窗口
    cur_window = self.driver.current_window_handle  # 获取当前窗口
    all_handles = self.driver.window_handles  # 获取所有窗口
    for handle in all_handles:
        if handle != cur_window:
            self.driver.switch_to.window(handle)
            self.driver.close()
    self.driver.switch_to.window(cur_window)


def refresh(self):
    self.driver.refresh()


def switch_driver(self, dr):
    self.driver = dr


def close(self):
    self.driver.close()