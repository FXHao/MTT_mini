# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")) + "/"
using(_project_root)
from channel.Channel import Channel

class tencent(Channel):
    
    def getProcessDict(self):
        return {}

    '''=============== 对应渠道流程相关 ================'''
    
    # 登录
    def login(self):
        sleep(10)
        for i in range(0, 10):
            pos = exists(Template(r"tpl1568186751566.png", record_pos=(-0.209, 0.673), resolution=(1080, 1920)))
            if (pos != False):
                keyevent("BACK")
                break
            sleep(1)
        sleep(1)
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
            return [poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout"), poco("com.outfit7.mytalkingtomfree:id/n2_t2_img"), poco("android:id/content").child("android.widget.FrameLayout").child("android.widget.RelativeLayout").child("com.outfit7.mytalkingtomfree:id/n2_t2_img")]
        
        if (PocoType == self.eCheckPoint["OrdinaryInterstitial_Close"]):  # 普通插屏_关闭
            return None
        
        if (PocoType == self.eCheckPoint["NativeInterstitial_Exist"]):    # 原生插屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["NativeInterstitial_Close"]):    # 原生插屏_关闭
            return None
        
        if (PocoType == self.eCheckPoint["Video_Exist"]):                 # Video_存在
            return poco("com.outfit7.mytalkingtomfree:id/tt_video_reward_container")
        
        if (PocoType == self.eCheckPoint["Video_End"]):                   # Video_结束
            return poco("com.outfit7.mytalkingtomfree:id/tt_video_ad_close")
        
        if (PocoType == self.eCheckPoint["Video_Close"]):                 # Video_关闭
            return poco("com.outfit7.mytalkingtomfree:id/tt_video_ad_close")
    
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
            return [Template(r"tpl1568793393481.png", record_pos=(0.416, -0.804), resolution=(1080, 1920)), Template(r"tpl1568793546434.png", record_pos=(-0.4, -0.802), resolution=(1080, 1920))]
        
        # Defalut
        return None

    
    
    

