#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter
import unittest
from conn.run_demo import RunMain
from hunter_interface.main.run_test import RunTestCase
import HTMLTestRunner
import json

class TestMethod(unittest.TestCase):    # 定义一个类，集成自unittest.TestCase

    def setUp(self):
        self.run = RunMain()
        self.run_test = RunTestCase()

    def test001(self):
        run = RunTestCase()
        run.go_run()

if __name__ == '__main__':
    filename = 'D:/hunter_/interfaceTest/hunter_interface/report/result.html'  # 测试报告存放的路径
    fp = open(filename, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test001'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试结果如下：')
    runner.run(suite)  # 执行存入套件中的测试用例
    fp.close()