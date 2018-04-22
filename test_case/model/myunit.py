#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/20 13:35
# @Author : Lanye
# @Site : 
# @File : myunit.py
# @Software: PyCharm

from selenium import webdriver
#from test_case.models.driver import browser
import unittest
import os

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()