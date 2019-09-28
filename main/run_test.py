#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter

from conn.run_demo import RunMain
from hunter_interface.data.handle_excel import *
from hunter_interface.data.logger import Logger
import json
from hunter_interface.base.runmethod import RunMain


class RunTestCase:
    def __init__(self):

        self.Runmain = RunMain()  # 实例化调用get/post请求基类
        self.data = HandleExcel()  # 实例化操作Excel文件类
        self.logger = Logger(__name__)

    def go_run(self):
        rows_count = self.data.get_rows()  # 获取Excel行数
        for i in range(1, rows_count):  # 利用行数进行迭代处理每个接口
            url = self.data.get_value(i, get_url())  # 循环获取URL的值
            method = self.data.get_value(i, get_mothod())  # 循环获取method的值
            print(self.data.get_value(i, get_params()))
            data = json.loads(self.data.get_value(i, get_params()))  # 循环获取请求参数
            expect = self.data.get_value(i, get_expectvalue())  # 循环获取期望输出
            is_run = self.data.get_value(i, get_priority())  # 获取是否运行，即判断Excel中priority是不是为“high"
            if is_run == 'high':
                res = self.Runmain.run_main(url, method, data)  # 调用主函数，res就是返回的参数
                self.logger.get_log().debug('第' + str(i) + '个接口的返回结果为：%s', res)  # 日志：输出接口响应内容
                self.data.write_value(i, get_actualvalue(), res)  # 将实际结果写入Excel中
                if expect in res:  # res返回的内容是否包含expect，是否与期望一致
                    # print('测试通过')
                    self.logger.get_log().error('第' + str(i) + '接口测试通过')
                    self.data.write_value(i, get_resultvalue(), 'pass')  # 调用写入数据方法，将结果写进Excel
                else:
                    # print("测试失败")
                    self.logger.get_log().info('第' + str(i) + '接口测试失败')
                    self.data.write_value(i, get_resultvalue(), 'fail')


if __name__ == '__main__':
    run = RunTestCase()
    run.go_run()
