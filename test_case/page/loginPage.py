#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/20 11:00
# @Author : Lanye
# @Site : 
# @File : loginPage.py
# @Software: PyCharm


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from test_case.page import basePage


class Login(basePage):
    '''用户登录页面'''

    url='/'

    #Action
    bbs_login_user_loc = (By.XPATH,"//div[@id='mzCust']/div/img")
    bbs_login_button_loc = (By.ID,"mzLogin")

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        self.find_element(*self.bbs_login_button_loc).click()

    login_username_loc = (By.ID,'account')
    login_password_loc = (By.ID,'password')
    login_button_loc = (By.ID,'login')

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_usepassword(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

     # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口
    def user_login(self,username='18025446964',password='L@nye.i99o'):
        '''获取的用户名密码登录'''
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_usepassword(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH,'//span[@for="account"]')
    pawd_error_hint_loc = (By.XPATH,'//span[@for="password"]')
    user_login_succedd_loc = (By.ID,"mzCustName")

    #用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    #密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_loc).text

    #登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_succedd_loc).text