# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../..")) + "/"
using(_project_root)
from abc import ABC,abstractmethod
from helper import exists_any

class Channel(ABC):
    
    MasterManager = None
    
    poco = None
    AppID = None
    Game = None
    
    Reporter = None
    
    '''==================== 初始化 ==================='''
    
    def __init__(self, TestMasterManager):
        self.MasterManager = TestMasterManager
        
    def config(self):
        self.poco = self.MasterManager.poco
        self.AppID = self.MasterManager.AppID
        self.Game = self.MasterManager.Game
        self.Reporter = self.MasterManager.Reporter

    # 修饰的父类不能实例化，但是继承的子类必须实现@abstractmethod装饰的方法
    @abstractmethod
    def getProcessDict(self):
        return None
    
    '''================= 获取识别信息 ================='''
    
    eCheckPoint = {"None": 0,

                   "OrdinarySplash_Exist": 1,
                   "OrdinarySplash_Close": 2,
                   "NativeSplash_Exist": 3,
                   "NativeSplash_Close": 4,
                    
                   "OrdinaryBanner_Exist": 5,
                   "NativeBanner_Exist": 6,

                   "OrdinaryInterstitial_Exist": 7,
                   "OrdinaryInterstitial_Close": 8,
                   "NativeInterstitial_Exist": 9,
                   "NativeInterstitial_Close": 10,
                   
                   "Video_Exist": 11,
                   "Video_End": 12,
                   "Video_Close": 13}
    
    ''' 返回相应监测点的Poco
        若该监测点不可使用Poco, 则返回None'''

    @abstractmethod
    def getPoco(self, PocoType = eCheckPoint["None"]):
        pass
    

    @abstractmethod
    def getImage(self, ImageType = eCheckPoint["None"]):
        ''' 返回相应监测点的Image List
            建议全部都填, 但是在有Poco的情况下不会用到图片
        '''
        pass
    

    def getPoco_default(self, PocoType = eCheckPoint["None"]):
        ''' 返回全渠道默认的相应监测点的Poco
            若该监测点不可使用Poco, 则返回None
        '''
        
        poco = self.poco
        
        if (PocoType == self.eCheckPoint["None"]):
            return None

        if (PocoType == self.eCheckPoint["OrdinarySplash_Exist"]):        # 普通开屏_存在
            return None

        if (PocoType == self.eCheckPoint["NativeSplash_Exist"]):          # 原生开屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["OrdinaryBanner_Exist"]):        # 普通Banner_存在
            return [poco(text="广告"), poco(nameMatches = "(.*)id/activead").offspring()]
        
        if (PocoType == self.eCheckPoint["NativeBanner_Exist"]):          # 原生Banner_存在
            return None
        
        if (PocoType == self.eCheckPoint["OrdinaryInterstitial_Exist"]):  # 普通插屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["NativeInterstitial_Exist"]):    # 原生插屏_存在
            return None
        
        if (PocoType == self.eCheckPoint["Video_End"]):                   # Video_结束
            return None
    
        return None
    

    def getImage_default(self, ImageType = eCheckPoint["None"]):
        ''' 返回全渠道默认的相应监测点的Image List
            建议全部都填, 但是在有Poco的情况下不会用到图片
        '''

        if (ImageType == self.eCheckPoint["OrdinarySplash_Exist"]):        # 普通开屏_存在
            return None

        if (ImageType == self.eCheckPoint["OrdinarySplash_Close"]):        # 普通开屏_关闭
            return None

        if (ImageType == self.eCheckPoint["OrdinaryBanner_Exist"]):        # 普通Banner_存在
            return [
                Template(r"tpl1567654232363.png", record_pos=(0.469, -1.019), resolution=(1080, 2248))]

        if (ImageType == self.eCheckPoint["OrdinaryInterstitial_Exist"]):  # 普通插屏_存在
            return [
                Template(r"tpl1567505512972.png", record_pos=(0.005, 0.424), resolution=(1080, 2248))]

        if (ImageType == self.eCheckPoint["Video_Close"]):                 # Video_关闭
            return [
                Template(r"tpl1565835360516.png", record_pos=(-0.226, 0.157), resolution=(720, 1280)),
                Template(r"tpl1565836077492.png", record_pos=(0.365, -0.934), resolution=(1080, 2340)),
                Template(r"tpl1565851739238.png", record_pos=(0.415, -0.806), resolution=(720, 1280)),
                Template(r"tpl1565836224911.png", record_pos=(0.412, -0.803), resolution=(720, 1280))
            ]

        # Defalut
        return None
    
    '''================= 广告识别相关 ================='''
    
    ''' 开屏是否存在 '''
    def isSplashExists(self, isReport = False):
        
        # 普通开屏(Poco)
        pos = exists_any(self.getPoco(self.eCheckPoint["OrdinarySplash_Exist"]))
        if (pos != False):
            self.Reporter.report("检测到普通开屏(Poco)", isReport_caller = isReport)
            sleep(10)
            return True
        
        # 原生开屏(Poco)
        pos = exists_any(self.getPoco(self.eCheckPoint["NativeSplash_Exist"]))
        if (pos != False):
            self.Reporter.report("检测到原生开屏(Poco)", isReport_caller = isReport)
            sleep(10)
            return True
        
        # 普通开屏(Default_Poco)
        pos = exists_any(self.getPoco_default(self.eCheckPoint["OrdinarySplash_Exist"]))
        if (pos != False):
            self.Reporter.report("检测到普通开屏(Default_Poco)", isReport_caller = isReport)
            sleep(10)
            return True
        
        # 普通开屏(图片)
        pos = exists_any(self.getImage(self.eCheckPoint["OrdinarySplash_Exist"]))
        if (pos != False):
            self.Reporter.report("检测到普通开屏(图片)", isReport_caller = isReport)
            sleep(10)
            return True
        
        # 原生开屏(图片)
        pos = exists_any(self.Game.nativeSplash)
        if (pos != False):
            self.Reporter.report("检测到原生开屏(图片)", isReport_caller = isReport)
            sleep(10)
            return True
        
        # 普通开屏(Default_图片)
        pos = exists_any(self.getImage_default(self.eCheckPoint["OrdinarySplash_Exist"]))
        if (pos != False):
            self.Reporter.report("检测到普通开屏(Default_图片)", isReport_caller = isReport)
            sleep(10)
            return True
        
        # 无开屏
        self.Reporter.report("未检测到开屏", isReport_caller = isReport)
        return False
        
    ''' Banner 是否存在
        若存在, 则输出存在并返回True
        若不存在则返回False '''
    def isBannerExists(self, isReport = False):
        
        checkpoint_list = [[self.Game.nativeBanner, "检测到原生Banner(图片)"],
                           [self.getPoco(self.eCheckPoint["OrdinaryBanner_Exist"]), "检测到普通Banner(Poco)"],
                           [self.getPoco(self.eCheckPoint["NativeBanner_Exist"]), "检测到原生Banner(Poco)"],
                           [self.getPoco_default(self.eCheckPoint["OrdinaryBanner_Exist"]), "检测到普通Banner(Default_Poco)"],
                           [self.getImage(self.eCheckPoint["OrdinaryBanner_Exist"]), "检测到普通Banner(图片)"],

                           [self.getImage_default(self.eCheckPoint["OrdinaryBanner_Exist"]), "检测到普通Banner(Default_图片)"]]
        
        for c, msg in checkpoint_list:
            pos = exists_any(c)
            if (pos != False):
                self.Reporter.report(msg, isReport_caller = isReport)
                return
        
        # 无Banner
        self.Reporter.report("未显示Banner", isReport_caller = isReport)
        return False
    
    ''' 跳过插屏广告
        若无插屏广告返回False
        若有插屏广告, 关闭插屏广告并放回True '''
    def skipInterstitial(self, isReport = False):
        
        sleep(4)
        
        checkpoint_list = [[self.getPoco(self.eCheckPoint["OrdinaryInterstitial_Exist"]),
                            self.getPoco(self.eCheckPoint["OrdinaryInterstitial_Close"]),
                            "检测到普通插屏(Poco)"],
                           [self.getPoco(self.eCheckPoint["NativeInterstitial_Exist"]),
                            self.getPoco(self.eCheckPoint["NativeInterstitial_Close"]),
                            "检测到原生插屏(Poco)"],
                           [self.getPoco_default(self.eCheckPoint["OrdinaryInterstitial_Exist"]),
                            self.getPoco_default(self.eCheckPoint["OrdinaryInterstitial_Close"]),
                            "检测到普通插屏(Default_Poco)"], 
                           [self.getImage(self.eCheckPoint["OrdinaryInterstitial_Exist"]), 
                            self.getImage(self.eCheckPoint["OrdinaryInterstitial_Close"]), 
                            "检测到普通插屏(图像)"], 
                           [self.Game.nativeInterstitial, 
                            self.Game.nativeInterstitialClose, 
                            "检测到原生插屏(图像)"], 
                           [self.getImage_default(self.eCheckPoint["OrdinaryInterstitial_Exist"]), 
                            self.getImage_default(self.eCheckPoint["OrdinaryInterstitial_Close"]), 
                            "检测到普通插屏(Default_图像)"]]
        
        for exist, close, msg in checkpoint_list:
            pos = exists_any(exist)
            if (pos != False):
                self.Reporter.report(msg, isReport_caller = isReport)
                pos = exists_any(close)
                if (pos != False):
                    touch(pos)
                else:
                    keyevent("BACK")
                return True
        
        # 无插屏
        if (isReport):
            self.Reporter.report("未显示插屏广告")
        return False
    
    ''' 跳过视频
        若无视频播放, 返回False
        若有视频播放, 等待视频结束并返回True '''
    def skipVideo(self, isReport = False):
        
        sleep(40)
        
        checkpoint_list = [[self.getPoco(self.eCheckPoint["Video_Close"]), "检测到视频(Poco)"],
                           [self.getPoco_default(self.eCheckPoint["Video_Close"]), "检测到视频(Default_Poco)"],
                           [self.getImage(self.eCheckPoint["Video_Close"]), "检测到视频(图片)"], 
                           [self.getImage_default(self.eCheckPoint["Video_Close"]), "检测到视频(Default_图片)"]]
        
        for close, msg in checkpoint_list:
            pos = exists_any(close)
            if (pos != False):
                self.Reporter.report(msg, isReport_caller = isReport)
                touch(pos)
                return True
        
        # No video exists
        if isReport:
            self.Reporter.report("未检测到视频")
        return False

    def skipBanner(self):
        pos = exists(Template(r"tpl1569661543760.png", record_pos=(0.356, -0.68), resolution=(1080, 1920)), )


    
    '''=============== 对应渠道流程相关 ================'''
    
    ''' 登录 '''
    @abstractmethod
    def login(self):
        pass
    
    ''' 重开游戏(未完) '''
    def restart(self):
        stop_app(self.AppID)
        start_app(self.AppID)
        self.login()
        
    '''================= 开发 Helper =================='''
    
    def print_CheckResult(self):
        print("Splash: " + self.isSplashExists().__str__())
        print("Banner: " + self.isSplashExists().__str__())
        print("Interstitial: " + self.isSplashExists().__str__())
        print("Interstitial Close: " + self.isSplashExists().__str__())
        print("Video: " + self.isVideoExists().__str__())

    def isCheckPointReady(self, checkpoint = "All"):
        
        isSplashReady = True
        isBannerReady = True
        isInterstitialReady = True
        isVideoReady = True
        
        if (self.getPoco(self.eCheckPoint["OrdinarySplash_Exist"]) == None and 
            self.getImage(self.eCheckPoint["OrdinarySplash_Exist"]) == None):
            isSplashReady = False
        
        if (self.getPoco(self.eCheckPoint["OrdinaryBanner_Exist"]) == None and 
            self.getImage(self.eCheckPoint["OrdinaryBanner_Exist"]) == None):
            isBannerReady == False
    
        if (self.getPoco(self.eCheckPoint["OrdinaryInterstitial_Exist"]) == None and
            self.getImage(self.eCheckPoint["OrdinaryInterstitial_Exist"]) == None):
            isInterstitialReady == False
        
        if ((self.getPoco(self.eCheckPoint["Video_Exist"]) == None or 
            self.getPoco(self.eCheckPoint["Video_End"]) == None) and
            self.getImage(self.eCheckPoint["Video_Close"]) == None):
            isVideoReady == False
        
        if (checkpoint == "All"):
            return isSplashReady and isBannerReady and isInterstitialReady and isVideoReady
        
        if (checkpoint == "Splash"):
            return isSplashReady
        
        if (checkpoint == "Banner"):
            return isBannerReady
        
        if (checkpoint == "Interstitial"):
            return isInterstitialReady
        
        if (checkpoint == "Video"):
            return isVideoReady
        


    


