# -*- coding: utf-8 -*-
from airtest.core.api import *

_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)

# 设置日志输出等级
import logging

logger = logging.getLogger('airtest')
logger.setLevel(logging.FATAL)
# logging.basicConfig(filename='test.log', level=logging.ERROR)
# logging.basicConfig(level=logging.ERROR, format='%(message)')


from AD.helper import exists_any
from AD.apkinfo import getpackagename
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)



class MyTalkingTom(object):
    def __init__(self):
        self.num = 10
        self.poco = poco
        self.game = input('请输入游戏：')
        self.channel = input('请输入渠道：')
        self.init_image()
        self.init_poco()
        self.packagename = None
        self.channel_poco = None
        self.mag_num = 0
        self.mag_path = '..//..//Reporter//mag'
        self.isOrdinarySplash = None
        self.isnativeSplash = None
        self.get_info()

    def init_poco(self):
        self.OPPO = None

        self.huawei = {
            'banner_p': self.poco(nameMatches='(.*)id/n1_t2_img'),
            'banner_p_close':self.poco(nameMatches='(.*)id/hiad_banner_close_button'),
            'banner_y': None,
            'interstitial_p': None,
            'interstitial_p_close': None,
            'interstitial_y': None,
            'interstitial_video': self.poco(nameMatches='(.*)id/interstitial_content_view'),
            'interstitial_video_close': self.poco(nameMatches='(.*)id/interstitial_close'),
            'video': self.poco(nameMatches='(.*)id/hiad_reward_view'),
            'video_close': self.poco(nameMatches='(.*)id/reward_close'),
            'isOrdinarySplash': True,
            'isNativeSplash': False,
        }

        self.vivo = None

        self.channel_dict = {
            '华为': self.huawei,
            'OPPO': self.OPPO,
            'vivo': self.vivo
        }

    def init_image(self):
        self.nativeBanner = [
            Template(r"tpl1569480707179.png", record_pos=(-0.306, -0.9), resolution=(1080, 2244)),
            Template(r"tpl1567505582092.png", record_pos=(-0.171, -0.874), resolution=(1080, 2248)),
            Template(r"tpl1568797914108.png", record_pos=(0.369, -0.818), resolution=(1080, 1920)),
            Template(r"tpl1568797924855.png", rgb=True, record_pos=(-0.374, -0.819), resolution=(1080, 1920)),
        ]

        self.nativeBannerClose = None

        self.nativeSplash = [
            Template(r"tpl1602754161372.png", record_pos=(-0.006, 0.656), resolution=(1200, 2640)),
            Template(r"tpl1569480920892.png", record_pos=(0.043, -0.35), resolution=(1080, 2244))
        ]

        self.nativeInterstitial = [
            Template(r"tpl1568798608788.png", record_pos=(-0.244, -0.028), resolution=(1080, 1920)),
            Template(r"tpl1567569523059.png", record_pos=(0.013, -0.473), resolution=(1080, 2248)),
            Template(r"tpl1569548730374.png", record_pos=(0.432, 0.049), resolution=(1080, 2244))
        ]

        self.nativeInterstitialClose = [
            Template(r"tpl1569483684083.png", record_pos=(0.392, -0.263), resolution=(1080, 2244)),
            Template(r"tpl1569548743261.png", record_pos=(0.367, -0.349), resolution=(1080, 2244))
        ]

        self.OrdinarySplash = [
            Template(r"tpl1567911842071.png", record_pos=(0.031, 0.77), resolution=(1080, 1920), threshold=0.6)
        ]


    def get_info(self):
        packagename = getpackagename(self.channel, self.game) # 包名
        channel_poco = self.channel_dict[self.channel]  # poco
        self.packagename = packagename
        self.channel_poco = channel_poco
        return packagename, channel_poco

    # 截图
    def snapshot_mag(self):
        '''截图'''
        self.mag_num += 1
        path = self.mag_path + '//{}.png'.format(self.mag_num)
        snapshot(filename=path)

    def process(self):
        process_dict = {
            '原生开屏': self.isOrdinarySplashExists(),
            '普通开屏': self
        }

    def isOrdinarySplashExists(self):
        '''检测普通开屏是否存在'''
        print("开始检测普通开屏")
        stop_app(self.packagename)
        sleep(2)
        for i in range(1, self.num + 1): # 检测不到时检测次数
            start_app(self.packagename)
            sleep(3)
            pos = exists_any(self.OrdinarySplash)
            if (pos == False):
                print('第{}次检测，未检测到普通开屏'.format(i))
                self.snapshot_mag()
                stop_app(self.packagename)
                continue
            self.isOrdinarySplash = True
            print("【检测到普通开屏】")
            self.snapshot_mag()
            return True
        if self.isnativeSplash == False:
            print("【未检测到普通开屏】")


    # 检测原生开屏
    def isNativeSplashExists(self):
        '''检测原生开屏是否存在'''
        pos1 = exists_any(self.nativeSplash)
        if (pos1 != False):
            self.isnativeSplash = True
            print("检测到原生开屏")
            self.snapshot_mag()
            return True
        return False





if __name__ == '__main__':
    a = MyTalkingTom()
    a.isOrdinarySplashExists()
    # a.snapshot_mag()