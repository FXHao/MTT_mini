# -*- encoding=utf8 -*-
__author__ = "wanghuajun"
from airtest.core.api import *
from airtest.core.android.minitouch import *
from airtest.core.android.rotation import XYTransformer
auto_setup(__file__)

def transform_xy(tuple_xy, display_info):
    x, y = tuple_xy
    x, y = XYTransformer.up_2_ori(
            (x, y),
            (display_info["width"], display_info["height"]),
            display_info["orientation"]
        )
    return x, y

class TouchEventHandler:
    
    '''
    # Demo

    t = TouchEventHandler()
    t.add_DownEvent([542, 1253])
    t.add_MoveEvent([495, 620])
    t.add_SleepEvent(2)
    t.add_UpEvent(finger = 0)
    t.perform()
    '''
    
    multitouch_event = []
    
    def __init__(self):
        self.multitouch_event = []
    
    # 按下
    def add_DownEvent(self, position, finger = 0):
        self.multitouch_event.append(DownEvent(transform_xy(position, device().display_info), finger))
        
    # 移动到
    def add_MoveEvent(self, position, finger = 0):
        self.multitouch_event.append(MoveEvent(transform_xy(position, device().display_info), finger))
    
    # 休眠
    def add_SleepEvent(self, time):
        self.multitouch_event.append(SleepEvent(time))
        
    # 抬起
    def add_UpEvent(self, finger = 0):
        self.multitouch_event.append(UpEvent(finger))
    
    ''' 运行 '''
    def perform(self):
        device().minitouch.perform(self.multitouch_event)
