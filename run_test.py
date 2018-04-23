#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/20 10:26
# @Author : Lanye
# @Site : 
# @File : run_test.py
# @Software: PyCharm

from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os


# ============================定义发生邮件=================================
def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("lanye.1990@163.com","L@nye.199o")
    smtp.sendmail("lanye.1990@163.com","lanye.1990@163.com",msg.as_string())
    smtp.quit()
    print("Email has send successful!")

# ============================查找测试报告目录，找到最新生成的测试报告=================================
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getatime(testreport + '\\' + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

# ============================定义发生邮件=================================
if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    filename = './report/' + now + 'result.html'

    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='window-firefox')
    discover = unittest.defaultTestLoader.discover('./test_case',pattern='*_sta.py')
    runner.run(discover)
    fp.close()

    file_path = new_report('./report')
    send_mail(file_path)
