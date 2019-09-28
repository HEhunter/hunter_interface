#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter

import time
from HTMLTestRunner import HTMLTestRunner
import unittest



def allCase():
    case_dir = 'D:/hunter_/interfaceTest/interface/case'  # 定义测试用例所在路径
    suite = unittest.TestSuite()  # 定义一个测试套件
    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern='test_*.py',
                                                   top_level_dir=None)

    """
    1、case_dir即测试用例所在目录
    2、patten='test_*.py' : 表示用例文件名的匹配规则，“*”表示任意多个字符，这里表示匹配所有以test_开头的文件
    3、top_level_dir=None : 测试模块的顶层目录。如果没顶层目录（也就是说测试用例不是放在多级目录中），默认为None
    """

    # discover方法筛选出来的用例，循环添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            suite.addTests(test_case)
    print(suite)
    '''直接加在discover'''
    return suite

if __name__ == '__main__':

    allsuit = allCase()
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = 'D:/hunter_/interfaceTest/hunter_interface/report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='接口测试报告',
                            description='Implementation Example with')
    runner.run(allsuit)
