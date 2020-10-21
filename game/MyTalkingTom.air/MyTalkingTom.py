# -*- encoding=utf8 -*-
from airtest.core.api import *

_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)

# 设置日志输出等级
import logging

logger = logging.getLogger('airtest')
logger.setLevel(logging.FATAL)
# logging.basicConfig(filename='test.log', level=logging.ERROR)
# logging.basicConfig(level=logging.ERROR, format='%(message)')


from game.helper import exists_any
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
from game.Reporter import reporter



class MyTalkingTom(object):

    def __init__(self):
        self.AppID = 'com.outfit7.mytalkingtomfree.HUAWEI'
        self.poco = poco
        self.scenes = None
        self.channel = '华为'
        self.reporter_msg = '存在'

        self.mag_num = 0
        self.mag_path = '..//Reporter//mag'
        self.Reporter_w = reporter.Reporter_excel()

        self.init_imglist()
        self.init_poco()
        self.init_Scenes()
        # self.num = 0

    def init_poco(self):
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

        self.vivo = {

            'banner_p': self.poco(nameMatches='(.*)id/n1_t2_img'),
            'banner_p_close': self.poco(nameMatches='(.*)id/n1_t2_img'),
            'interstitial_p': self.poco(nameMatches='(.*)id/n1_t2_img'),
            'interstitial_p_close': self.poco(nameMatches='(.*)id/n1_t2_img'),
            'video': self.poco(nameMatches='(.*)id/n1_t2_img'),
            'video_close': self.poco(nameMatches='(.*)id/n1_t2_img'),
        }

    def init_Scenes(self):
        self.Livingroom = {
            'banner_p': 'A10',
            'banner_y': 'B10',
            'interstitial_p': 'C10',
            'interstitial_y': 'D10',
            'interstitial_v': 'E10',
            'video': 'F10'
        }

        self.Kitchen = {
            'banner_p': 'A14',
            'banner_y': 'B14',
            'interstitial_p': 'C14',
            'interstitial_y': 'D14',
            'interstitial_v': 'E14',
            'video': 'F14'
        }

        self.Bathroom = {
            'banner_p': 'A18',
            'banner_y': 'B18',
            'interstitial_p': 'C18',
            'interstitial_y': 'D18',
            'interstitial_v': 'E18',
            'video': 'F18'
        }

        self.Bedroom = {
            'banner_p': 'A22',
            'banner_y': 'B22',
            'interstitial_p': 'C22',
            'interstitial_y': 'D22',
            'interstitial_v': 'E22',
            'video': 'F22'
        }

        self.Paypage = {
            'banner_p': 'A26',
            'banner_y': 'B26',
            'interstitial_p': 'C26',
            'interstitial_y': 'D26',
            'interstitial_v': 'E26',
            'video': 'F26'
        }

    def get_Scenes(self, scenes=None):
        ''''''
        scenes_dict = {
            'Livingroom': self.Livingroom,
            'Kitchen': self.Kitchen,
            'Bathroom': self.Bathroom,
            'Bedroom': self.Bedroom,
            'Paypage': self.Paypage
        }
        return scenes_dict[scenes]

    def get_channel(self, channel=None):
        '''返回对应渠道poco'''
        channel_d = {
            '华为': self.huawei,
            'vivo': self.vivo
        }

        return channel_d[channel]

    def init_imglist(self, Point=None):
        self.nativeBanner = [
            Template(r"tpl1569480707179.png", record_pos=(-0.306, -0.9), resolution=(1080, 2244)),
            Template(r"tpl1567505582092.png", record_pos=(-0.171, -0.874), resolution=(1080, 2248)),
            Template(r"tpl1568797914108.png", record_pos=(0.369, -0.818), resolution=(1080, 1920)),
            Template(r"tpl1568797924855.png", rgb=True, record_pos=(-0.374, -0.819), resolution=(1080, 1920)),
        ]

        self.nativeBannerClose = [

        ]

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
            Template(r"tpl1567911842071.png", record_pos=(0.031, 0.77), resolution=(1080, 1920))
        ]


    '''==================== 检测banner部分START ===================='''
    # 检测普通banner
    def isOrdinaryBannerExists(self, scenes):
        '''检测普通banner'''
        poco_dict = self.get_channel(channel=self.channel)
        # OrdinaryBanner_poco = poco_dict['banner_p']
        # if OrdinaryBanner_poco is None:
        #     print("{}渠道无普通banner".format(self.channel))
        #     return False

        po = exists_any(poco_dict['banner_p'])
        if (po == False):
            return False
        self.Reporter_w.write_excel(scenes['banner_p'], self.reporter_msg)
        print("检测到普通banner")
        self.snapshot_mag()
        po_close = exists_any(poco_dict['banner_p_close'])
        if (po_close != False):
            po_close.click()
        return True

    # 检测原生banner
    def isNativeBannerExists(self, scenes):
        '''检测原生banner'''
        # poco_dict = self.get_channel(channel=self.channel)
        # NativeBanner_poco = poco_dict['banner_y']
        # if NativeBanner_poco is None:
        #     print("{}渠道无原生banner".format(self.channel))
        #     return False

        pos = exists_any(self.nativeBanner)
        if (pos == False):
            return False
        self.Reporter_w.write_excel(scenes['banner_y'], self.reporter_msg)
        print("检测到原生banner")
        self.snapshot_mag()
        pos_close = exists_any(self.nativeBannerClose)
        if (pos_close != False):
            touch(pos_close)
        return True

    # 检测banner
    def isBannerExists(self):
        '''检测banner'''
        print("【开始检测banner】")
        scenes = self.get_Scenes(self.scenes)
        poco_dict = self.get_channel(channel=self.channel)
        NativeBanner_poco = poco_dict['banner_y']
        OrdinaryBanner_poco = poco_dict['banner_p']
        for i in range(4):
            if OrdinaryBanner_poco is None:
                print("{}渠道无普通banner".format(self.channel))
            else:
                self.isOrdinaryBannerExists(scenes)

            if NativeBanner_poco is None:
                print("{}渠道无原生banner".format(self.channel))
            else:
                self.isNativeBannerExists(scenes)

    '''==================== 检测banner部分END ===================='''


    '''==================== 检测开屏广告部分START ===================='''
    # 检测普通开屏
    def isOrdinarySplashExists(self):
        '''检测普通开屏是否存在'''

        pos = exists_any(self.OrdinarySplash)
        if (pos != False):
            self.Reporter_w.write_excel('A6', '存在')
            print("检测到普通开屏")
            self.snapshot_mag()
            return True
        return False

    # 检测原生开屏
    def isNativeSplashExists(self):
        '''检测原生开屏是否存在'''
        pos1 = exists_any(self.nativeSplash)
        if (pos1 != False):
            self.Reporter_w.write_excel('B6', '存在')
            print("检测到原生开屏")
            self.snapshot_mag()
            return True
        return False

    # 检测开屏广告
    def isSplashExists(self):
        '''
        检测开屏广告
        Ordinary：是否需要重复检测普通开屏（重复20次），默认开启
        Native：是否需要重复检测原生开屏，默认开启
        '''
        print("【开始检测开屏广告】")
        OrdinarySplash = self.isOrdinarySplashExists()
        NativeSplash = self.isNativeSplashExists()

        poco_dict = self.get_channel(channel=self.channel)
        Ordinary = poco_dict['isOrdinarySplash']
        Native = poco_dict['isNativeSplash']

        if (Ordinary == True):
            for i in range(20):
                if (OrdinarySplash == True):
                    break
                sleep(5)
                print('未检测到普通开屏，准备第{}次重启检测'.format(i))
                self.stop_app()
                sleep(2)
                self.start_app()
                OrdinarySplash = self.isOrdinarySplashExists()

        if (Native == True):
            for i in range(20):
                if (NativeSplash == True):
                    break
                sleep(5)
                print('未检测到原生开屏，准备第{}次重启检测'.format(i))
                self.stop_app()
                sleep(2)
                self.start_app()
                NativeSplash = self.isNativeSplashExists()

    '''==================== 检测开屏广告部分END ===================='''


    '''==================== 检测插屏广告部分START ===================='''
    # 检测普通插屏
    def isOrdinaryInterstitialExists(self, scenes):
        '''检测普通插屏'''
        # scenes = self.get_Scenes(scenes='Livingroom')
        poco_dict = self.get_channel(channel=self.channel)
        OrdinaryInterstitial_poco = poco_dict['interstitial_p']
        if OrdinaryInterstitial_poco is None:
            print("{}渠道无普通插屏".format(self.channel))
            return False

        po = exists_any(poco_dict['interstitial_p'])
        if (po == False):
            return False
        self.Reporter_w.write_excel(scenes['interstitial_p'], self.reporter_msg)
        print("检测到普通插屏")
        self.snapshot_mag()
        po_close = exists_any(poco_dict['interstitial_p_close'])
        if po_close != False:
            po_close.click()
        else:
            keyevent('BACK')
        return True

    # 检测原生插屏
    def isNativeInterstitialExists(self, scenes):
        '''检测原生插屏'''
        poco_dict = self.get_channel(channel=self.channel)
        p = poco_dict['interstitial_y']
        if p is None:
            print("{}渠道无原生插屏".format(self.channel))
            return False

        pos = exists_any(self.nativeInterstitial)
        if (pos == False):
            return False
        self.Reporter_w.write_excel(scenes['interstitial_y'], self.reporter_msg)
        print("检测到原生插屏")
        self.snapshot_mag()
        pos_close = exists_any(self.nativeInterstitialClose)
        if pos == False:
            keyevent("BACK") # 虽然不管用，但只能点点看~
        else:
            touch(pos_close)
        return True

    # 检测视频插屏
    def isVideoInterstitialExists(self, scenes):
        '''检测视频插屏'''
        poco_dict = self.get_channel(channel=self.channel)
        VideoInterstitial_poco = poco_dict['interstitial_video']
        if VideoInterstitial_poco is None:
            print("{}渠道无视频插屏".format(self.channel))
            return False

        po = exists_any(poco_dict['interstitial_video'])
        if (po == False):
            return False
        self.Reporter_w.write_excel(scenes['interstitial_v'], self.reporter_msg)
        print("检测到视频插屏")
        self.snapshot_mag()
        po_close = exists_any(poco_dict['interstitial_video_close'])
        if (po_close == False):
            keyevent('BACK')
        else:
            po_close.click()
        return True

    # 检测插屏广告
    def isInterstitialExists(self):
        '''检测插屏'''
        print("【开始检测插屏广告】")
        scenes = self.get_Scenes(self.scenes)

        inter_p = self.isOrdinaryInterstitialExists(scenes)
        inter_y = self.isNativeInterstitialExists(scenes)
        iner_v = self.isVideoInterstitialExists(scenes)

        if (inter_y or inter_p or iner_v) == False:
            return False
        return True

    '''==================== 检测插屏广告部分END ===================='''


    '''==================== 检测视频广告部分START ===================='''
    # 检测视频广告
    def isVideoExists(self):
        '''检测视频广告'''
        print('【开始检测视频广告】')
        poco_dict = self.get_channel(channel=self.channel)
        scenes = self.get_Scenes(self.scenes)
        po = exists_any(poco_dict['video'])
        if (po == False):
            return False
        self.Reporter_w.write_excel(scenes['video'], self.reporter_msg)
        print("检测到视频广告")
        self.snapshot_mag()
        sleep(30)
        po_close = exists_any(poco_dict['video_close'])
        po_close_Button = poco_dict['video_close']
        if (po_close == False):
            keyevent("BACK")
        else:
            po_close_Button.click()
        return True

    '''==================== 检测视频广告部分END ===================='''

    # 截图
    def snapshot_mag(self):
        '''截图'''
        self.mag_num += 1
        path = self.mag_path + '//{}.png'.format(self.mag_num)
        snapshot(filename=path)

    '''==================== 游戏基础操作 ===================='''
    # 游戏基础操作
    def start_app(self):
        print("正在启动游戏....")
        start_app(self.AppID)
        # sleep(2)

    def stop_app(self):
        print('正在关闭游戏...')
        stop_app(self.AppID)

    def clear_app(self):
        print('正在清除数据...')
        clear_app(self.AppID)
        sleep(5)

    def wake_phone(self):
        wake()
        sleep(2)

    '''==================== 跳过部分 ===================='''

    # 跳过用户协议
    def skip_useragreement(self):
        '''跳过用户协议'''
        print('跳过用户协议')
        sleep(3)
        pos = exists(Template(r"tpl1602324183519.png", record_pos=(0.171, 0.437), resolution=(1080, 2340)))
        if (pos != False):
            touch(pos)

    # 跳过权限
    def skip_permission(self, times=3):
        '''跳过权限'''
        print('跳过权限')
        poco = self.poco
        sleep(2)
        for i in range(0, times):
            if poco(text="始终允许").exists():
                poco(text="始终允许").click()
                sleep(2)
                continue
            if poco(text="允许").exists():
                poco(text="允许").click()
                sleep(2)
                continue
            if poco(text="确定").exists():
                poco(text="确定").click()
                sleep(2)
                continue

    # 跳过新手礼包
    def skip_beginner_gift(self):
        '''跳过新手礼包'''
        pos = exists_any([
            Template(r"tpl1567506478562.png", record_pos=(0.33, 0.508), resolution=(1080, 2248)),
            Template(r"tpl1602323710044.png", record_pos=(-0.079, -0.444), resolution=(1200, 2640))
        ])
        if (pos == False):
            return
        # touch(Template(r"tpl1567506495302.png", record_pos=(0.406, -0.835), resolution=(1080, 2248)))
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
        pos = exists_any(Template(r"tpl1597912633490.png", record_pos=(0.006, -0.286), resolution=(1080, 2340)))
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
        sleep(3)
        touch(Template(r"tpl1567501638079.png", record_pos=(0.383, 0.022), resolution=(1080, 2248)), duration=0.5,
              times=2)
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
        swipe(Template(r"tpl1567503796792.png", record_pos=(-0.278, 0.215), resolution=(1080, 2248)),
              Template(r"tpl1567504346592.png", record_pos=(0.0, 0.025), resolution=(1080, 2248)))
        sleep(5)
        touch(Template(r"tpl1567503827541.png", record_pos=(0.207, 0.928), resolution=(1080, 2248)))
        sleep(15)
        touch(Template(r"tpl1567503851190.png", record_pos=(-0.198, 0.926), resolution=(1080, 2248)))
        swipe(Template(r"tpl1567503873365.png", record_pos=(0.024, 0.152), resolution=(1080, 2248)),
              vector=[0.0184, 0.1791])
        sleep(5)
        touch(Template(r"tpl1567503882284.png", record_pos=(0.404, 0.919), resolution=(1080, 2248)))
        touch(Template(r"tpl1567503897930.png", record_pos=(0.406, 0.659), resolution=(1080, 2248)))
        sleep(20)
        touch(Template(r"tpl1569826643419.png", record_pos=(0.425, -0.81), resolution=(720, 1280)))
        sleep(10)
        touch(Template(r"tpl1567504671526.png", record_pos=(0.402, 0.66), resolution=(1080, 2248)))

    # 跳过新手教程
    def skip_beginner_guide(self):
        '''跳过新手教程'''
        print("跳过新手")
        sleep(10)
        pos = exists_any(Template(r"tpl1567501638079.png", record_pos=(0.383, 0.022), resolution=(1080, 2248)))
        if (pos == False):
            return
        touch(pos, duration=0.5, times=2)
        sleep(1)
        touch(Template(r"tpl1567501771358.png", rgb=True, record_pos=(0.001, 0.401), resolution=(1080, 2248)))
        sleep(3)
        pos1 = exists_any([
            Template(r"tpl1602572841304.png", record_pos=(0.003, 0.183), resolution=(1200, 2640)),
            Template(r"tpl1602931632398.png", record_pos=(0.357, -0.859), resolution=(1080, 2310)),
        ])
        for i in range(2):
            if (pos1 != False):
                # touch(Template(r"tpl1602492999405.png", record_pos=(0.36, -0.879), resolution=(1200, 2640)))
                touch(pos1)
            sleep(3)
            self.skip_luying()
            sleep(3)

    # 检测是否在主界面
    def check_isMainPage(self):
        '''检测是否在主界面'''
        sleep(3)
        pos = exists_any([
            Template(r"tpl1570517004453.png", record_pos=(0.302, 0.055), resolution=(1080, 2280)), # 客厅
            Template(r"tpl1568259166153.png", record_pos=(-0.297, -0.195), resolution=(1080, 1920)), # 厨房
            Template(r"tpl1568259303064.png", record_pos=(-0.113, -0.244), resolution=(1080, 1920), threshold=0.8), # 浴室
            Template(r"tpl1597907023319.png", record_pos=(-0.03, -0.4), resolution=(1080, 2280))  # 卧室
        ])
        # print(pos)
        if (pos == False):
            return False
        return True

    # 操作界面不主界面时应该执行的操作
    def isNoMainPage_do(self):
        '''操作界面不主界面时应该执行的操作'''
        if (self.check_isMainPage() == False):
            print("不在主界面")
            # pos1 = exists_any(Template(r"tpl1602572841304.png", record_pos=(0.003, 0.183), resolution=(1200, 2640)))
            # if (pos1 != False):
            # # touch(Template(r"tpl1602492999405.png", record_pos=(0.36, -0.879), resolution=(1200, 2640)))
            #     touch(pos1)
            self.skip_luying()
            if (self.check_isMainPage() == False):
                self.skip_daily_discount()
                self.skip_beginner_gift()
                self.skip_daily_challenge()
                if (self.check_isMainPage() == False):
                    # TODO：检测插屏广告视频广告
                    self.isInterstitialExists()
                    if (self.check_isMainPage() == False):
                        keyevent("BACK")
                        if (self.check_isMainPage() == False):
                            keyevent("BACK")
                            if (self.check_isMainPage() == False):
                                assert_equal(True, False, "未知当前界面位置，将重启游戏")
                                print("未知当前界面位置，将重启游戏")
                                # self.main()
                                # TODO：不知位置后的操作

    # 前往客厅
    def goToLivingroom(self):
        print("前往客厅")
        sleep(3)
        for i in range(4):
            pos = exists_any([
                Template(r"tpl1567667429838.png", record_pos=(-0.203, 0.922), resolution=(1080, 2248)),
                Template(r"tpl1567667416052.png", record_pos=(-0.194, 0.92), resolution=(1080, 2248)),
                Template(r"tpl1567589317467.png", record_pos=(-0.196, 0.925), resolution=(1080, 2248)),
                Template(r"tpl1567589396053.png", record_pos=(-0.198, 0.925), resolution=(1080, 2248)),
                Template(r"tpl1596538199151.png", record_pos=(-0.194, 0.948), resolution=(1080, 2340))
            ])
            if (pos == False):
                # assert_equal(True, False, "goToLivingroom() 客厅按钮未找到.")
                print("客厅按钮未找到")
                self.isNoMainPage_do()
            for j in range(0, 5):
                touch(pos)
                self.scenes = 'Livingroom'
                sleep(0.5)
                # self.isNoMainPage_do()
                self.isBannerExists()

    # 前往厨房
    def goToKitchen(self):
        sleep(3)
        for i in range(4):
            pos = exists_any([
                Template(r"tpl1567577528299.png", record_pos=(0.0, 0.919), resolution=(1080, 2248)),
                Template(r"tpl1567667454466.png", record_pos=(0.005, 0.92), resolution=(1080, 2248)),
                Template(r"tpl1597905990964.png", record_pos=(0.002, 0.923), resolution=(1080, 2280)),
                Template(r"tpl1567589340484.png", record_pos=(-0.001, 0.923), resolution=(1080, 2248)),
                Template(r"tpl1567589388744.png", record_pos=(-0.001, 0.924), resolution=(1080, 2248))
            ])
            if (pos == False):
                # assert_equal(True, False, "goToKitchen() 厨房按钮未找到.")
                self.isNoMainPage_do()
            for i in range(0, 10):
                touch(pos)
                self.scenes = 'Kitchen'
                sleep(0.5)
                # self.isNoMainPage_do()
                self.isBannerExists()


    # 前往浴室
    def goToBathroom(self):
        sleep(3)
        pos = exists_any([
            Template(r"tpl1567506551693.png", record_pos=(0.196, 0.919), resolution=(1080, 2248)),
            Template(r"tpl1567664748415.png", record_pos=(0.197, 0.92), resolution=(1080, 2248)),
        ])
        if (pos == False):
            # assert_equal(True, False, "goToBathroom() 测试按钮未找到.")
            # return
            self.isNoMainPage_do()
        for i in range(0, 10):
            touch(pos)
            self.scenes = 'Bathroom'
            self.isBannerExists()

    # 前往卧室
    def goToBedroom(self):
        sleep(3)
        pos = exists_any([
            Template(r"tpl1567506283133.png", record_pos=(0.401, 0.919), resolution=(1080, 2248)),
            Template(r"tpl1567589362374.png", record_pos=(0.401, 0.923), resolution=(1080, 2248)),
            Template(r"tpl1567589372396.png", record_pos=(0.397, 0.919), resolution=(1080, 2248))
        ])
        if (pos == False):
            # assert_equal(True, False, "goToBedroom() 卧室按钮未找到.")
            # return
            self.isNoMainPage_do()

        for i in range(0, 10):
            touch(pos)
            self.scenes = 'Bedroom'
            self.isBannerExists()

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
                    self.isNoMainPage_do()

    # 前往充值界面
    def goToPay(self):
        '''前往充值界面'''
        pos = exists(Template(r"tpl1568190300263.png", record_pos=(-0.144, -0.582), resolution=(1080, 1920)))
        if (pos == False):
            return


    def first_open(self):
        '''主程序逻辑'''
        self.stop_app()
        self.clear_app()
        # 启动
        self.start_app()
        # 跳过用户协议
        self.skip_useragreement()
        # 跳过权限
        self.skip_permission()
        # 跳过新手教程
        self.skip_beginner_guide()
        # self.beginner_guide()





if __name__ == '__main__':
    MTT = MyTalkingTom()
    # MTT.check_banner()
    # MTT.start_app()
    # MTT.main()
    # MTT.check_Splash_Exists()
    # MTT.check_Banner_Exists()
    MTT.first_open()
    MTT.goToLivingroom()
    MTT.goToKitchen()
    # print(MTT.check_isMainPage())
