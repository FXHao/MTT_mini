# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)
from channel.Channel import Channel
from helper import exists_any

class vivo(Channel):
    
    def getProcessDict(self):
        return {}
    
    '''=============== 对应渠道流程相关 ================'''
    
    # 登录
    def login(self):
        poco = self.poco
        for i in range(0, 10):
            pos = exists(Template(r"tpl1569825847886.png", record_pos=(-0.214, 0.676), resolution=(720, 1280)))
            if (pos != False):
                touch(pos)
                break
            sleep(2)
        sleep(5)
        self.Game.skip_beginner_gift()
    
    '''================= Poco Getter ================='''
    
    def getPoco(self, PocoType = Channel.eCheckPoint["None"]):

        poco = self.poco

        if (PocoType == self.eCheckPoint["None"]):
            return None

        if (PocoType == self.eCheckPoint["OrdinarySplash_Exist"]):        # 普通开屏_存在
            # return None
            return [
                poco(text='我的汤姆猫'),
                poco(nameMatches = '(.*)id/tt_splash_ad_gif')
            ]

        if (PocoType == self.eCheckPoint["OrdinarySplash_Close"]):        # 普通开屏_关闭
            # return None
            return [poco(nameMatches = '(.*)id/tt_splash_skip_btn')]

        if (PocoType == self.eCheckPoint["NativeSplash_Exist"]):          # 原生开屏_存在
            return None

        if (PocoType == self.eCheckPoint["NativeSplash_Close"]):          # 原生开屏_关闭
            return None

        if (PocoType == self.eCheckPoint["OrdinaryBanner_Exist"]):        # 普通Banner_存在
            return [
                poco(text="广告"),
                poco("com.outfit7.mytalkingtom.vivo:id/banner_layout")
            ]

        if (PocoType == self.eCheckPoint["NativeBanner_Exist"]):          # 原生Banner_存在
            return None

        if (PocoType == self.eCheckPoint["OrdinaryInterstitial_Exist"]):  # 普通插屏_存在
            return None

        if (PocoType == self.eCheckPoint["OrdinaryInterstitial_Close"]):  # 普通插屏_关闭
            return None

        if (PocoType == self.eCheckPoint["NativeInterstitial_Exist"]):    # 原生插屏_存在
            return None

        if (PocoType == self.eCheckPoint["NativeInterstitial_Close"]):    # 原生插屏_关闭
            return None

        if (PocoType == self.eCheckPoint["Video_End"]):                   # Video_结束
            return [poco(text="关闭视频")]

        if (PocoType == self.eCheckPoint["Video_Close"]):                 # Video_关闭
            return None

        return None
    
    def getImage(self, ImageType = Channel.eCheckPoint["None"]):
        
        if (ImageType == self.eCheckPoint["OrdinarySplash_Exist"]):        # 普通开屏_存在
            return None
        
        if (ImageType == self.eCheckPoint["OrdinarySplash_Close"]):        # 普通开屏_关闭
            return None
        
        if (ImageType == self.eCheckPoint["OrdinaryBanner_Exist"]):        # 普通Banner_存在
            return [
                Template(r"tpl1567654232363.png", record_pos=(0.469, -1.019), resolution=(1080, 2248))
            ]
        
        if (ImageType == self.eCheckPoint["OrdinaryInterstitial_Exist"]):  # 普通插屏_存在
            return [
                Template(r"tpl1567505512972.png", record_pos=(0.005, 0.424), resolution=(1080, 2248)),
                Template(r"tpl1569480761122.png", record_pos=(0.001, 0.36), resolution=(1080, 2244))
            ]
        
        if (ImageType == self.eCheckPoint["OrdinaryInterstitial_Close"]):  # 普通插屏_关闭
            return [
                Template(r"tpl1567505512972.png", record_pos=(0.005, 0.424), resolution=(1080, 2248)),
                Template(r"tpl1569480761122.png", record_pos=(0.001, 0.36), resolution=(1080, 2244))
            ]
        
        if (ImageType == self.eCheckPoint["Video_Close"]):                 # Video_关闭
            return [
                Template(r"tpl1565835360516.png", record_pos=(-0.226, 0.157), resolution=(720, 1280)),
                Template(r"tpl1565836077492.png", record_pos=(0.365, -0.934), resolution=(1080, 2340)),
                Template(r"tpl1565851739238.png", record_pos=(0.415, -0.806), resolution=(720, 1280)),
                Template(r"tpl1565836224911.png", record_pos=(0.412, -0.803), resolution=(720, 1280))
            ]

        # Defalut
        return None
    
    

