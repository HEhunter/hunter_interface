#!/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__: hunter

import xlrd
from xlutils.copy import copy


class HandleExcel:
    """封装操作Excel的方法"""

    def __init__(self, file='D:/hunter_/interfaceTest/hunter_interface/case/demo2.xlsx', sheet_id=0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()
        # 为了创建一个实例时就获得Excel的sheet对象，可以在构造器中调用get_data()
        # 因为类在实例化时就会自动调用构造器，这样创建一个实例时就会自动获得sheet对象了

    # 获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id)
        return sheet

    # 获取Excel数据行数
    def get_rows(self):
        rows = self.data.nrows

        return rows

    # 获取某个单元格写入数据
    def get_value(self, row, col):
        value = self.data.cell_value(row, col)
        return value

    # 向某个单元格写入数据
    def write_value(self, row, col, value):
        data = xlrd.open_workbook(self.file)  # 打开文件
        data_copy = copy(data)  # 复制源文件
        sheet = data_copy.get_sheet(0)  # 取得复制文件的sheet对象
        sheet.write(row, col, value)  # 在某一单元格写入value
        data_copy.save(self.file)  # 保存文件


# 封装Excel的列名常量
# 测试用例编号
def get_caseNmber():
    caseNmber = 0
    return caseNmber


# 用例类型
def get_caseType():
    caseType = 1
    return caseType


def get_caseName():
    caseName = 2
    return caseName


# 优先级
def get_priority():
    priority = 3
    return priority


def get_url():
    url = 4
    return url


def get_mothod():
    mothod = 5
    return mothod


def get_header():
    header = 6
    return header


# 测试用例目的
def get_purpose():
    purpose = 7
    return purpose


def get_params():
    params = 8
    return params


# 预期结果
def get_expectvalue():
    expectvalue = 9
    return expectvalue


# 实际结果
def get_actualvalue():
    actualvalue = 10
    return actualvalue


# 用例是否通过
def get_resultvalue():
    resultvalue = 11
    return resultvalue


if __name__ == '__main__':
    test = HandleExcel()
    print(test.get_data())
    print(test.get_rows())
    print(test.get_value(1, 11))
