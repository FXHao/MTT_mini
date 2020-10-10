# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
auto_setup(__file__)
using(_project_root)
from channel.Channel import Channel
from helper import exists_any

class cps(Channel):
    
    def getProcessDict(self):
        return {}

    '''=============== 对应渠道流程相关 ================'''
    
    # 登录
    def login(self):
        sleep(20)
        for i in range(1, 10):
            pos = exists_any([Template(r"tpl1568883448109.png", record_pos=(0.381, 0.02), resolution=(1080, 1920)), Template(r"tpl1568883477317.png", record_pos=(-0.397, 0.765), resolution=(1080, 1920))])
            if (pos != False):
                break
            else:
                keyevent("BACK")
                sleep(2)
    
    '''================= Poco Getter ================='''

    def getPoco(self, PocoType = Channel.eCheckPoint["None"]):
        
        poco = self.poco
        
        if (PocoType == self.eCheckPoint["None"]):
            return None
        
        if (PocoType == self.eCheckPoint["OrdinarySplash_Exist"]):        # 普通开屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["OrdinarySplash_Close"]):        # 普通开屏_关闭
            return None
        
        if (PocoType == self.eCheckPoint["NativeSplash_Exist"]):          # 原生开屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["NativeSplash_Close"]):          # 原生开屏_关闭
            return None
        
        if (PocoType == self.eCheckPoint["OrdinaryBanner_Exist"]):        # 普通Banner_存在
            return poco("com.outfit7.mytalkingtomfree:id/activead").offspring()
        
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
        
        if (PocoType == self.eCheckPoint["Video_Exist"]):                 # Video_存在
            return None
        
        if (PocoType == self.eCheckPoint["Video_End"]):                   # Video_结束
            return None
        
        if (PocoType == self.eCheckPoint["Video_Close"]):                 # Video_关闭
            return None
    
        return None

    def getImage(self, ImageType = Channel.eCheckPoint["None"]):
        
        if (ImageType == self.eCheckPoint["OrdinarySplash_Exist"]):        # 普通开屏_存在
            return None
        
        if (ImageType == self.eCheckPoint["OrdinarySplash_Close"]):        # 普通开屏_关闭
            return None
        
        if (ImageType == self.eCheckPoint["OrdinaryBanner_Exist"]):        # 普通Banner_存在
            return None
        
        if (ImageType == self.eCheckPoint["OrdinaryInterstitial_Exist"]):  # 普通插屏_存在
            return [Template(r"tpl1569553748075.png", record_pos=(0.381, -0.197), resolution=(1080, 2244)), Template(r"tpl1569555124714.png", record_pos=(0.381, -0.196), resolution=(1080, 2244))]
        
        if (ImageType == self.eCheckPoint["OrdinaryInterstitial_Close"]):  # 普通插屏_关闭
            return [Template(r"tpl1569553748075.png", record_pos=(0.381, -0.197), resolution=(1080, 2244)), Template(r"tpl1569555124714.png", record_pos=(0.381, -0.196), resolution=(1080, 2244))]
        
        if (ImageType == self.eCheckPoint["Video_Close"]):                 # Video_关闭
            return [Template(r"tpl1569553846189.png", record_pos=(0.369, -0.2), resolution=(2244, 1080))]
        
        # Defalut
        return None
    

