# -*- encoding=utf8 -*-
'''
auther = "linzhifan"
date = "2019-10-23"
'''

import os
import xlrd

channerdict = {
    "华为": ["华为", 6],
    "OPPO": ["OPPO", 22],
    "vivo": ["vivo", 25],
}

gamenamedict = {
    'MTT': ['MTT', 1],
    'TTHD': ['TTHD', 5],
    'MTA': ['MTA', 2],
    'TTC': ['TTC', 8],
    'TG2': ['TG2', 10],
    'TTJ': ['咪咕TTJ', 6],
    'TT2': ['TT2', 12],
    'TT': ['TT', 11],
    'MTH': ['MTH', 3],
    'TA': ['TA', 13],
    'MTTF': ['MTTF', None], # 暂未添加
    'TTGR': ['TTGR', 15],
    'MTT2': ['MTT2', 4],
    'TTCR': ['TTCR', 7],
    'TTP': ['TTP', 9]
}

def getpackagename(row, col):
    '''
    获取表格中的包名
    :param row: 行号  int
    :param col: 列号  int
    :return xl_packagename： 获取到的包名
    '''
    # xlsx_path = 'C://Users//acer//Desktop//packagename.xlsx'
    path = os.path.abspath(os.path.dirname(__file__)) + "//"
    xlsx_path = path + 'packagename.xlsx'
    xlsx_data = xlrd.open_workbook(xlsx_path)
    table = xlsx_data.sheet_by_name('Sheet1')
    if row is None:
        print('该渠道在表格中还未设置！')
        xl_packagename = None
        return xl_packagename
    if col is None:
        print('该游戏在表格中还未设置')
        xl_packagename = None
        return xl_packagename
    xl_packagename = table.cell_value(channerdict[row][1], gamenamedict[col][1])
    return xl_packagename