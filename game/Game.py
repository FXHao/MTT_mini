# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../..")) + "/"
from abc import ABC, abstractmethod
using(_project_root)

class Game(ABC):
    
    MasterManager = None
    
    poco = None
    AppID = None
    Channel = None
    
    Reporter = None

    '''==================== 初始化 ==================='''
    
    def __init__(self, MasterManager):
        self.MasterManager = MasterManager
        
    def config(self):
        self.poco = self.MasterManager.poco
        self.AppID = self.MasterManager.AppID
        self.Channel = self.MasterManager.Channel
        self.Reporter = self.MasterManager.Reporter
        
    @abstractmethod
    def getProcessDict(self):
        pass
        
    '''=================== 通用流程 =================='''
    
    def start_app(self):
        start_app(self.AppID)
        sleep(25)
        
    def stop_app(self):
        stop_app(self.AppID)
        sleep(3)
        
    def clear_app(self):
        clear_app(self.AppID)
        sleep(3)

    def wake_phone(self):
        wake()
        sleep(2)
