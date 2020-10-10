# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../..")) + "/"

eTestCaseState = {"Function Not Found": -1,
                  "UnInitialized": 0,
                  "Function Configered": 1,
                  "Test Successed": 2,
                  "Test Failed": 3}

class TestCase:
    
    ID = None
    name = "Undefined"
    args = []
    test_function = None
    
    State = eTestCaseState["UnInitialized"]
    
    Result = None
    Message = ""
    
    # 初始化
    def __init__(self, ID = None, name = "Undefined", args = []):
        
        if (ID == None):
            raise Exception("Invalid ID", ID)
            
        self.ID = ID
        self.name = name
        self.args = args
        self.test_function = None
        self.State = eTestCaseState["UnInitialized"]
    
    # 输出为字符串
    def __str__(self):
        result = ('ID：%d\tName：%s\tArgs:' %(self.ID,self.name)) + self.args.__str__()
        result += "\nFunction: " + self.test_function.__str__()
        return result
    
    # 设置测试函数
    def setTestFunction(self, test_function = None):
        
        self.test_function = test_function
        
        if (test_function == False):
            self.State = eTestCaseState["Function Not Found"]
        else:
            self.State = eTestCaseState["Function Configered"]
    
    ''' 运行测试 '''
    def run_test(self):
        self.test_function()
    
    # [Helper] 测试开始运行时执行
    def onTestBegin(self):
        pass

    # [Helper] 测试成功时执行
    def onTestSuccess(self):
        self.State = eTestCaseState["Test Successed"]
        self.CaseSummarize_print()
    
    # [Helper] 测试失败时执行
    def onTestFailed(self):
        self.State = eTestCaseState["Test Failed"]
        self.CaseSummarize_print()
    
    ''' 打印测试总结 '''
    def CaseSummarize_print(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(self.CaseSummarize_str())
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
    ''' 获取测试总结 '''
    def CaseSummarize_str(self):
        result = self.__str__() + "\n"
        
        if (self.State == eTestCaseState["Function Not Found"]):
            result += "Function Not Found\n"
            
        if (self.State == eTestCaseState["UnInitialized"]):
            result += "UnInitialized\n"
            
        if (self.State == eTestCaseState["Function Configered"]):
            result += "Function Configered\n"
            
        if (self.State == eTestCaseState["Test Successed"]):
            result += "\nTest Successed\n"
            result += self.Message
            
        if (self.State == eTestCaseState["Test Failed"]):
            result += "Test Failed\n"

        return result
    
    
    
    
    
