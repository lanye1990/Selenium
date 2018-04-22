#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/20 11:01
# @Author : Lanye
# @Site : 
# @File : login_sta.py
# @Software: PyCharm

import unittest,random
import time
from test_case.model import myunit,prtscr
from test_case.page.mailpage import MailLogin


class loginTest(myunit.MyTest):
    '''社区登录测试'''

    p_url = 'https://mail.163.com/'
    #p_url='http://www.baidu.com'

    #测试用户登录
    def user_login_verify(self,username = '',password = ''):
        MailLogin(self.driver).user_login(username,password,self.p_url)

    # 账户密码不能为空提示
    def test_login1(self):
        '''用户名、密码不能为空'''
        print(self.driver.title)
        self.user_login_verify()
        # 声明MailLogin对象
        po = MailLogin(self.driver)
        self.assertEqual(po.login_error_hint(), '请输入账号')
        prtscr.screenShot(self.driver, 'user_pwd_empty.jpg')

    # 密码不能为空提示
    def test_login2(self):
        # 用户名正确，密码为空测试
        self.user_login_verify(username='lanye.1990@163.com')
        po = MailLogin(self.driver)
        self.assertEqual(po.login_error_hint(), '请输入密码')
        prtscr.screenShot(self.driver, 'pwd_empty.jpg')

    # 账号不能为空提示
    def test_login3(self):
        # 用户名为空，密码正确测试
        self.user_login_verify(username='L@nye.199o')
        po = MailLogin(self.driver)
        self.assertEqual(po.login_error_hint(), '请输入账号')
        prtscr.screenShot(self.driver, 'user_empty.jpg')

    # 账户密码不匹配
    def test_login4(self):
        # 用户名、密码不匹配
        character = random.choice('abcdefghijklmn')
        username = 'rand' + character
        self.user_login_verify(username=username, password="123456")
        po = MailLogin(self.driver)
        self.assertEqual(po.login_error_hint(), '账号或密码错误')
        prtscr.screenShot(self.driver, 'user_pwd_error.jpg')

    #账户密码正确
    def test_login5(self):
        '''用户名、密码正确'''
        self.user_login_verify(username='lanye.1990',password='L@nye.199o')
        #声明MailLogin对象
        po = MailLogin(self.driver)
        self.assertEqual(po.login_success(),'lanye.1990@163.com')

    if __name__ == '__main__':
        unittest.main()




