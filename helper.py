# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.proxy import UIObjectProxy
from airtest.core.android.minitouch import *
from airtest.core.android.rotation import XYTransformer

# 检测是否存在图片或poco
def exists_any(obj):
    
    # 若为空
    if (obj == None):
        return False
    
    # 若对象为图片
    if (type(obj) == Template):
        return exists(obj)
    
    # 若对象为poco
    if (type(obj) == UIObjectProxy):
        try:
            if (obj.exists()):
                return position_to_absolute(obj.get_position())
            else:
                return False
        except:
            return False
    
    # 若对象为列表
    if (type(obj) == list):
        for item in obj:
            result = exists_any(item)
            if (result != False):
                return result
        return False

def transform_xy(tuple_xy, display_info):
    x, y = tuple_xy
    x, y = XYTransformer.up_2_ori(
            (x, y),
            (display_info["width"], display_info["height"]),
            display_info["orientation"]
        )
    return x, y

# 根据相对位置获得绝对位置
def position_to_absolute(relative_position):
    x, y = relative_position
    width = device().display_info["width"]
    height = device().display_info["height"]
    return (x * width), (y * height)
    
# 根据绝对位置获得相对位置
def position_to_relative(absolute_position):
    x, y = absolute_position
    width = device().display_info["width"]
    height = device().display_info["height"]
    return (x / width), (y / height)

# Touch Event
class TouchEventHandler:
    
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

    
    
    
    
    
    
    
    
    
    