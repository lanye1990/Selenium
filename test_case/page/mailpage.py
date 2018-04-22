#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/20 10:58
# @Author : Lanye
# @Site : 
# @File : mailpage.py
# @Software: PyCharm

from selenium import webdriver
from test_case.page.basePage import Page
from selenium.webdriver.common.by import By
import time

class MailLogin(Page):
    '''邮箱登录页面'''

    #定位iframe
    frame_loc = 'x-URS-iframe'

    #定位用户名、密码及登录按钮
    login_username_loc = (By.CSS_SELECTOR,'input[name="email"]')
    login_password_loc = (By.CSS_SELECTOR,'input[name="password"]')
    login_button_loc = (By.CSS_SELECTOR,'#dologin')

    #定位用户名、密码提示语
    login_error_loc = (By.CSS_SELECTOR,'ferrorhead')

    #定位登陆成功
    login_success_loc = (By.CSS_SELECTOR,'#spnUid')
    #切换frame
    def switchTologinFrame(self):
        self.switch_frame(self.frame_loc)

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_usepassword(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

     # 登录按钮
    def login_button(self):
        t = self.find_element(*self.login_button_loc).text
        print(t)
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口
    def user_login(self,username,password,url):
        '''获取的用户名密码登录'''
        self.open(url)
        self.switchTologinFrame()
        self.login_username(username)
        self.login_usepassword(password)
        self.login_button()
        time.sleep(1)

    #登录失败提示
    def login_error_hint(self):
        return self.find_element(*self.login_error_loc).text

    #登录成功
    def login_success(self):
        return self.find_element(*self.login_success_loc).text