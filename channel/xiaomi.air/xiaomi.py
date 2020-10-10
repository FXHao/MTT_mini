# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)
from channel.Channel import Channel

class xiaomi(Channel):
    
    def getProcessDict(self):
        return {}
    
    '''=============== 对应渠道流程相关 ================'''
    
    # 登录
    def login(self):
        sleep(15)
        if (exists(Template(r"tpl1568272687649.png", record_pos=(-0.001, -0.003), resolution=(1080, 1920)))):
            keyevent("BACK")
            touch(Template(r"tpl1568272806918.png", record_pos=(0.309, 0.139), resolution=(1080, 1920)))
            sleep(10)
        self.Game.skip_beginner_gift()
    
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
            return poco("com.outfit7.mytalkingtomfree:id/activead").child("android.widget.FrameLayout")
        
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
            return None
        
        if (ImageType == self.eCheckPoint["OrdinaryInterstitial_Close"]):  # 普通插屏_关闭
            return None
        
        if (ImageType == self.eCheckPoint["Video_Close"]):                 # Video_关闭
            return [Template(r"tpl1568273093443.png", record_pos=(0.414, -0.802), resolution=(1080, 1920)), Template(r"tpl1568273153036.png", record_pos=(0.413, -0.804), resolution=(1080, 1920))]
        
        # Defalut
        return None
    
