# -*- coding: utf-8 -*-

import openpyxl
import os



class Reporter_excel(object):

    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(__file__)) + "//"
        self.template_path = self.path + 'report_template.xlsx'
        self.report_path = self.path + 'reporter.xlsx'
        self.title = '广告测试'
        self.isFirstOpen = True

    # def create_excel(self):
    #     self.book = openpyxl.Workbook()
    #     self.sheet = self.book.active
    #
    #     self.sheet.title = self.title
    #     self.sheet['A1'] = '渠道'
    #     self.sheet['A2'] = '游戏'
    #
    #     self.sheet['A4'] = '客厅'
    #     self.sheet['A5'] = '普通开屏'
    #     self.sheet['B5'] = '原生开屏'
    #     self.sheet['C5'] = '普通banner'
    #     self.sheet['D5'] = '原生banner'
    #     self.sheet['E5'] = '普通插屏'
    #     self.sheet['F5'] = '原生插屏'
    #     self.sheet['G5'] = '视频插屏'
    #     self.sheet['H5'] = '视频'
    #
    #     # self.sheet[]
    #
    #     self.book.save(self.path)


        # self.sheet['A4'] = ''
        # self.sheet['A4'] = ''
        # self.sheet['A4'] = ''
        # self.sheet['A4'] = ''
        # self.sheet['A4'] = ''
        # self.sheet['A4'] = ''

    def read_excel(self):
        wb = openpyxl.load_workbook(self.template_path)
        sheet = wb[self.title]

        data = sheet['A1'].value
        print(data)

    def write_excel(self, cell=None, data=None):
        if self.isFirstOpen == True:
            wb = openpyxl.load_workbook(self.template_path)
            self.isFirstOpen = False
        else:
            wb = openpyxl.load_workbook(self.report_path)
        sheet = wb[self.title]
        sheet[cell] = data
        wb.save(self.report_path)

# b = Reporter()
# b.write_excel('B1', 'huawe')