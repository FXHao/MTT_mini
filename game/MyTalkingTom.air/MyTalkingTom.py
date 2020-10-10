# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)
from game.Game import Game
from helper import exists_any, position_to_absolute
import traceback

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


class MyTalkingTom(object):
    '''
    游戏内容
    '''

    def __init__(self):
        self.AppID = 'com.outfit7.mytalkingtomfree'
        self.poco = poco

    # 游戏基础操作
    def start_app(self):
        start_app(self.AppID)

    def stop_app(self):
        stop_app(self.AppID)

    def clear_app(self):
        clear_app(self.AppID)

    def wake_phone(self):
        wake()
        sleep(2)


    '''==================== 跳过部分 ===================='''

    # 跳过用户协议
    def skip_useragreement(self):
        '''跳过用户协议'''
        pos = exists(Template(r"tpl1602324183519.png", record_pos=(0.171, 0.437), resolution=(1080, 2340)))
        if (pos != False):
            try:
                touch(pos)
            except:
                return

    # 跳过权限
    def skip_permission(self, times = 10):
        '''跳过权限'''
        poco = self.poco
        for i in range(0, times):
            if poco(text = "始终允许").exists():
                poco(text = "始终允许").click()
                sleep(2)
                continue
            if poco(text = "允许").exists():
                poco(text = "允许").click()
                sleep(2)
                continue
            if poco(text = "确定").exists():
                poco(text = "确定").click()
                sleep(2)
                continue

    # 跳过新手礼包
    def skip_beginner_gift(self):
        '''跳过新手礼包'''
        sleep(2)
        pos = exists_any([
            Template(r"tpl1567506478562.png", record_pos=(0.33, 0.508), resolution=(1080, 2248)),
            Template(r"tpl1602323710044.png", record_pos=(-0.079, -0.444), resolution=(1200, 2640))
        ])
        if (pos != False):
            try:
                touch(Template(r"tpl1567506495302.png", record_pos=(0.406, -0.835), resolution=(1080, 2248)))
            except:
                keyevent("BACK")


    # 跳过每日挑战
    def skip_daily_challenge(self):
        '''跳过每日挑战'''
        pos = exists(Template(r"tpl1568704252875.png", record_pos=(0.004, -0.448), resolution=(1080, 1920)))
        if (pos == False):
            return
        keyevent("BACK")

    # 跳过每日优惠
    def skip_daily_discount(self):
        '''跳过每日优惠'''
        pos = exists(Template(r"tpl1597912633490.png", record_pos=(0.006, -0.286), resolution=(1080, 2340)))
        if (pos == False):
            return
        keyevent("BACK")

    # 录音权限
    def skip_luying(self):
        self.skip_permission()



    '''==================== 游戏内容部分 ===================='''

    # 新手过程
    def beginner_guide(self):
        '''新手引导'''
        touch(Template(r"tpl1567501638079.png", record_pos=(0.383, 0.022), resolution=(1080, 2248)), duration=0.5, times = 2)
        sleep(1)
        touch(Template(r"tpl1567501771358.png", rgb=True, record_pos=(0.001, 0.401), resolution=(1080, 2248)))
        sleep(5)
        pos = exists(Template(r"tpl1567504064721.png", record_pos=(0.02, 0.386), resolution=(1080, 2248)))
        if (pos != False):
            touch(pos)
            touch(Template(r"tpl1567504157962.png", record_pos=(-0.126, 0.362), resolution=(1080, 2248)))
            sleep(5)
        touch(Template(r"tpl1567503757543.png", record_pos=(0.008, 0.465), resolution=(1080, 2248)))
        sleep(3)
        touch(Template(r"tpl1567503778397.png", record_pos=(0.006, 0.925), resolution=(1080, 2248)))
        swipe(Template(r"tpl1567503796792.png", record_pos=(-0.278, 0.215), resolution=(1080, 2248)), Template(r"tpl1567504346592.png", record_pos=(0.0, 0.025), resolution=(1080, 2248)))
        sleep(5)
        touch(Template(r"tpl1567503827541.png", record_pos=(0.207, 0.928), resolution=(1080, 2248)))
        sleep(15)
        touch(Template(r"tpl1567503851190.png", record_pos=(-0.198, 0.926), resolution=(1080, 2248)))
        swipe(Template(r"tpl1567503873365.png", record_pos=(0.024, 0.152), resolution=(1080, 2248)), vector=[0.0184, 0.1791])
        sleep(5)
        touch(Template(r"tpl1567503882284.png", record_pos=(0.404, 0.919), resolution=(1080, 2248)))
        touch(Template(r"tpl1567503897930.png", record_pos=(0.406, 0.659), resolution=(1080, 2248)))
        sleep(20)
        touch(Template(r"tpl1569826643419.png", record_pos=(0.425, -0.81), resolution=(720, 1280)))
        sleep(10)
        touch(Template(r"tpl1567504671526.png", record_pos=(0.402, 0.66), resolution=(1080, 2248)))

    # 前往客厅
    def goToLivingroom(self, isReportInterstitial = False, isReportVideo = False):
        pos = exists_any([
            Template(r"tpl1567667429838.png", record_pos=(-0.203, 0.922), resolution=(1080, 2248)),
            Template(r"tpl1567667416052.png", record_pos=(-0.194, 0.92), resolution=(1080, 2248)),
            Template(r"tpl1567589317467.png", record_pos=(-0.196, 0.925), resolution=(1080, 2248)),
            Template(r"tpl1567589396053.png", record_pos=(-0.198, 0.925), resolution=(1080, 2248)),
            Template(r"tpl1596538199151.png", record_pos=(-0.194, 0.948), resolution=(1080, 2340))
        ])
        if (pos == False):
            # assert_equal(True, False, "goToLivingroom() 客厅按钮未找到.")
            log('goToLivingroom() 客厅按钮未找到')
            return
        for i in range(0, 10):
            try:
                touch(pos)
            except:
                # TODO: 无按钮时需处理
                pass
            sleep(1)
            pos2 = exists_any([
                Template(r"tpl1570517004453.png", record_pos=(0.302, 0.055), resolution=(1080, 2280)),
                Template(r"tpl1597747615936.png", record_pos=(0.051, -0.426), resolution=(1080, 2340))
            ])
            if (pos2 == False):
                # Todo: 需要检测和跳过的流程

                keyevent("BACK")

    # 前往厨房
    def goToKitchen(self, isReportInterstitial = False, isReportVideo = False):
        pos = exists_any([
            Template(r"tpl1567577528299.png", record_pos=(0.0, 0.919), resolution=(1080, 2248)),
            Template(r"tpl1567667454466.png", record_pos=(0.005, 0.92), resolution=(1080, 2248)),
            Template(r"tpl1597905990964.png", record_pos=(0.002, 0.923), resolution=(1080, 2280)),
            Template(r"tpl1567589340484.png", record_pos=(-0.001, 0.923), resolution=(1080, 2248)),
            Template(r"tpl1567589388744.png", record_pos=(-0.001, 0.924), resolution=(1080, 2248))
        ])
        if (pos == False):
            assert_equal(True, False, "goToKitchen() 厨房按钮未找到.")
            return
        for i in range(0, 10):
            touch(pos)
            sleep(0.5)
            pos2 = exists(Template(r"tpl1568259166153.png", record_pos=(-0.297, -0.195), resolution=(1080, 1920)))
            if (pos2 == False):
                # Todo: 需要检测和跳过的流程
                pass

    # 前往浴室
    def goToBathroom(self, isReportInterstitial = False, isReportVideo = False):
        pos = exists_any([
            Template(r"tpl1567506551693.png", record_pos=(0.196, 0.919), resolution=(1080, 2248)),
            Template(r"tpl1567664748415.png", record_pos=(0.197, 0.92), resolution=(1080, 2248)),
            Template(r"tpl1597906407997.png", record_pos=(0.197, 0.924), resolution=(1080, 2280)),
            Template(r"tpl1597906451619.png", record_pos=(0.2, 0.931), resolution=(1080, 2280)),
            Template(r"tpl1597906510673.png", record_pos=(0.206, 0.928), resolution=(1080, 2280))
        ])
        if (pos == False):
            assert_equal(True, False, "goToBathroom() 测试按钮未找到.")
            return
        for i in range(0, 10):
            touch(pos)
            sleep(0.5)
            pos2 = exists(Template(r"tpl1568259303064.png", record_pos=(-0.113, -0.244), resolution=(1080, 1920)))
            if (pos2 == False):
                # Todo: 需要检测和跳过的流程
                pass

    # 前往卧室
    def goToBedroom(self, isReportInterstitial = False, isReportVideo = False):
        pos = exists_any([
            Template(r"tpl1567506283133.png", record_pos=(0.401, 0.919), resolution=(1080, 2248)),
            Template(r"tpl1567589362374.png", record_pos=(0.401, 0.923), resolution=(1080, 2248)),
            Template(r"tpl1567589372396.png", record_pos=(0.397, 0.919), resolution=(1080, 2248))
        ])
        if (pos == False):
            assert_equal(True, False, "goToBedroom() 卧室按钮未找到.")
            return
        for i in range(0, 10):
            touch(pos)
            sleep(0.5)
            # pos2 = exists(Template(r"tpl1568259388088.png", record_pos=(-0.003, 0.323), resolution=(1080, 1920)))
            pos2 = exists_any([
                Template(r"tpl1568259388088.png", record_pos=(-0.003, 0.323), resolution=(1080, 1920)),
                Template(r"tpl1597907023319.png", record_pos=(-0.03, -0.4), resolution=(1080, 2280))
            ])
            if (pos2 == False):
                # Todo: 需要检测和跳过的流程
                pass

    # 返回主界面
    def backToMain(self):
        '''返回主界面'''
        for i in range(0, 5):
            pos = exists(Template(r"tpl1568254696587.png", record_pos=(-0.399, 0.769), resolution=(1080, 1920)))
            if (pos != False):
                for j in range(0, 5):
                    pos = exists_any([
                        Template(r"tpl1567667429838.png", record_pos=(-0.203, 0.922), resolution=(1080, 2248)),
                        Template(r"tpl1567667416052.png", record_pos=(-0.194, 0.92), resolution=(1080, 2248)),
                        Template(r"tpl1567589317467.png", record_pos=(-0.196, 0.925), resolution=(1080, 2248)),
                        Template(r"tpl1567589396053.png", record_pos=(-0.198, 0.925), resolution=(1080, 2248)),
                        Template(r"tpl1596538199151.png", record_pos=(-0.194, 0.948), resolution=(1080, 2340))
                    ])
                    if (pos == False):
                        break
                    touch(pos)
                    pos2 = exists(Template(r"tpl1568195750810.png", record_pos=(0.349, -0.102), resolution=(1080, 1920)))
                    if (pos2 == False):
                        pass


if __name__ == '__main__':
    MTT = MyTalkingTom()
    MTT.start_app()
    sleep(2)
    MTT.skip_useragreement()
    sleep(2)
    MTT.skip_permission()
    sleep(2)
    MTT.beginner_guide()
    sleep(2)
    MTT.goToLivingroom()





