#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/4/20 10:52
# @Author : Lanye
# @Site : 
# @File : basePage.py
# @Software: PyCharm

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver
#from assertpy import assert_that
import os

"""
Page类封装所有页面都公用的方法
"""


class Page(object):
    def __init__(self, driver):
        # 初始化变量
        self.driver = driver
        self.timeout = 30

    def _open(self, url):
        # _开头为私有方法，import *时不会被导入
        self.driver.get(url)
        self.driver.maximize_window
        self.driver.implicitly_wait(10)
        # 断言页面是否打开
        #assert self._open(), "Did not land on %s" % url

    def open(self, base_url):
        # 定义open方法，调用_open()进行打开链接
        self._open(base_url)

    def find_element(self, *loc):
        # 重写元素定位方法
        try:
            # 确保元素是可见的
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s 页面中未能找到   %s 元素" % (self, loc))

    def find_elements(self, *loc):
        # 重写元素定位方法,定位一组元素
        try:
            # 确保元素是可见的
            WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            print("%s 页面中未能找到   %s 元素" % (self, loc))

    def is_element_exist(self, *loc):
        # 判断元素是否被找到
        flag = True
        try:
            self.driver.find_element(*loc)
            return flag
        except:
            flag = False
            return flag

    def is_elements_exist(self, *loc):
        # 判断元素是否被找到
        flag = True
        try:
            self.driver.find_elements(*loc)
            return flag
        except:
            flag = False
            return flag

    def is_element_visible(self, loc):
        # 判断元素是否显示
        flag = True
        try:
            the_element = EC.visibility_of_element_located(loc)
            assert the_element(self.driver)
            return flag
        except:
            flag = False
            return flag

    def switch_frame(self, loc):
        # 重写switch_frame方法
        return self.driver.switch_to.frame(loc)

    def switch_default(self):
        # 跳出frame
        self.driver.switch_to_default_content()

    def get_current_window(self):
        # 获取当前窗口句柄
        current_win = self.driver.current_window_handle
        return current_win

    def get_all_windows(self):
        # 获取所有窗口句柄
        all_win = self.driver.window_handles
        return  all_win

    def switch_window(self, hdl):
        self.driver.switch_to.window(hdl)

    def script(self, src):
        # 定义script方法，用于执行js脚本，返回执行结果
        self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        # 重新定义send_keys方法
        try:
            loc = getattr(self, "_%s" % loc)
            print(loc)
            if click_first:
                self.find_element(*loc).clear()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s 页面中未能找到   %s 元素" % (self, loc))

    def select_value(self, loc, value):
        # 定义select方法
        sel = self.driver.find_element(*loc)
        return Select(sel).select_by_value(value)

    def actions_focus(self, loc):
        # 鼠标悬停
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(loc)
        actions.perform()

    def actions_click(self, loc):
        # 鼠标点击
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(loc)
        actions.click(loc)
        actions.perform()

    def accept_alert(self):
        # 处理页面警告窗，判断是否有弹窗，有则-确定并返回弹窗提示信息
        flag = False
        result = EC.alert_is_present()(self.driver)
        if result:
            print(result.text)
            self.driver.switch_to_alert().accept()
            flag = True
        else:
            print("alert 未弹出！")
            flag = False
        return flag

    def accept_cancel(self):
        # 处理页面弹窗，无法用工具定位的弹窗-取消
        self.driver.switch_to_alert().dismiss()

    def scroll_topByid(self, var):
        # 通过id定位让浏览器滚动条处理-滚到顶部
        js = "var q = document.getElementById('" + var + "').scrollTop = 0"
        return self.script(js)

    def scroll_footByid(self, var):
        # 通过id定位让浏览器滚动条处理-滚到底部
        js = "var q = document.getElementById('" + var + "').scrollTop = 10000"
        return self.script(js)

    def scroll_footByClass(self, var):
        # 通过class定位让浏览器滚动条处理-滚到底部
        js = "document.getElementsByClassName('" + var + "')[0].scrollTop = 10000"
        return self.script(js)

    def scroll_foot(self):
        js = "var q=document.body.scrollTop=100000"
        return self.script(js)

    def lstrip_str(self, strs, var):
        # 删除左边开头
        return strs.lstrip(var)

    def assert_title(self, var):
        # 断言题目是否正确
        assert_that(self.driver.title).is_equal_to(var)

    def searchFileDelete(self, filePath, keys):
        # 删除文件
        for filename in os.listdir(filePath):
            fp = os.path.join(filePath, filename)
            if os.path.isfile(fp) and keys in filename:
                os.remove(fp)

    def searchFile(self, filePath, keys):
        # 搜索目录下包含keys的文件
        flag = False
        for filename in os.listdir(filePath):
            fp = os.path.join(filePath, filename)
            if os.path.isfile(fp) and keys in filename:
                print
                fp
                os.remove(fp)
                flag = True
                break
            else:
                flag = False

        if flag is False:
            print("文件不存在！")
        return flag