# -*- encoding=utf8 -*-
__author__ = "wanghuajun"

from airtest.core.api import *
_project_root = os.path.abspath(os.path.join(os.path.abspath(__file__), "../..")) + "/"
print(_project_root)
auto_setup(__file__)
using(_project_root)
from airtest.core.android.adb import ADB
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import configparser
import types
import traceback
from TestManager.TestCase import TestCase, eTestCaseState
from TestManager.TestReporter import TestReporter

class MasterManager:

    poco = None
    AppID = None
    Game = None
    Channel = None
    Reporter = None
    
    ModuleGetter = None

    TestCaseList = None
    ProcessDictList = None
    
    curCase = None
    NoneCase = TestCase(ID = -1, name = "NoneCase", args = [])
    
    LogFileName = "Unnamed.txt"
    
    
    def __init__(self):
        self.poco = AndroidUiautomationPoco(force_restart=False)
        self.curCase = self.NoneCase
        self.Reporter = TestReporter(self)
    
    ''' 配置测试 '''
    def config(self, config_file = ""):
        
        # 配置Module
        config = configparser.ConfigParser()
        config.read(os.path.dirname(os.path.abspath(__file__)) + "/../" + config_file)
        self.config_module(config)
        
        # 配置流程
        self.LogFileName = "Log1.txt"
        self.config_process("process.CSV")
        
    # [Helper] 配置Module
    def config_module(self, config):
        
        # 配置文件
        self.AppID = config["jinke"]["package_name"]    # apk包名
        game_name = config["jinke"]["game_name"]        # 游戏名称
        channel = config["jinke"]["channel"]            # 渠道

        self.config_game(game_name)
        self.config_channel(channel)

        self.Game.config()
        self.Channel.config()
        self.get_ProcessDictFromModule()
    
    # [Helper] 配置Game
    def config_game(self, game_name):
        using(_project_root + "game/" + game_name + ".air")
        gameModule = __import__(game_name)
        self.Game = getattr(gameModule,game_name)(self)
    
    # [Helper] 配置Channel
    def config_channel(self, channel):
        try:
            using(_project_root + "channel/" + channel + ".air")
            channelModule = __import__(channel)
            self.Channel = getattr(channelModule, channel)(self)
            self.Reporter.report("Channel: " + channel)
        except:
            using(_project_root + "channel/emptychannel.air")
            channelModule = __import__("emptychannel")
            self.Channel = getattr(channelModule, "emptychannel")(self)
            self.Reporter.report("Channel: " + "emptychannel")

    # [Helper]
    def get_ProcessDictFromModule(self):
        '''
        从各个Module获取流程字典
        '''
        self.ProcessDictList = []
        self.ProcessDictList.append(self.Game.getProcessDict()) # 游戏相关流程
        self.ProcessDictList.append(self.Channel.getProcessDict())  # 渠道相关流程

    # [Helper] 配置流程
    def config_process(self, process_control_file = None):
        '''
        配置流程
        :param process_control_file: process.CSV
        '''
        
        if (process_control_file == None or process_control_file == ""):
            # raise Exception("Invalid process control file name", process_control_file)
            raise Exception("无效的流程控制文件！", process_control_file)

        # 初始化
        self.TestCaseList = []
        curID = 0
        
        # 读取文件
        with open(_project_root + process_control_file, "r") as csvParse:
            for line in csvParse:
                
                # 获得每一行数据
                fields = line.split(',')
                for i in range(0, len(fields)):
                    fields[i] = fields[i].strip()

                # 创建并添加新TestCase
                case = None
                test_name = fields[0]
                if (test_name != ""):
                    args = []
                    for i in range(1, len(fields)):
                        if (fields[i] != ""):
                            args.append(fields[i])
                    case = TestCase(ID = curID, name = test_name, args = args)
                    case.setTestFunction(self.get_ProcessFunction(key = test_name))
                    curID += 1
                else:
                    continue
                    
                self.TestCaseList.append(case)
        return


    # [Helper]
    def get_ProcessFunction(self, key = "None"):
        '''
        通过字典获取对应函数
        '''
        for dic in self.ProcessDictList:
            if (key in dic):
                return dic[key]
            continue
        return False
    
    ''' 打印流程列表 '''
    def print_test_list(self):
        if (self.TestCaseList == None):
            print(None)
            return
        for case in self.TestCaseList:
            print(case)
        return
    
    ''' 打印流程字典 '''
    def print_process_dicts(self):
        for dic in self.ProcessDictList:
            print(dic)
        
    ''' 运行流程 '''
    def run_test(self):
        for case in self.TestCaseList:
            
            self.curCase = case
        
            if (case.State != eTestCaseState["Function Configered"]):
                continue

            case.onTestBegin()
            try:
                case.run_test()
                case.onTestSuccess()
            except:
                case.onTestFailed()
                traceback.print_exc()
                if (case.name == "Guide"):
                    break
                self.Channel.restart()
    
    ''' 打印流程总结 '''
    def TestSummarize_print(self):
        print(self.TestSummarize_str())

    ''' 获得流程总结 '''
    def TestSummarize_str(self):
        result = "Test Summarize:\n\n"
        for case in self.TestCaseList:
            result += "\n"
            result += case.CaseSummarize_str()
            result += "\n"
        
        result += "================================\n"
        result += "注: 失败的测试指流程执行失败\n"
        total_case = 0
        success_case = 0
        fail_case = 0
        fun_not_found_case = 0
        other_case = 0
        
        for case in self.TestCaseList:
            if (case.State == eTestCaseState["Function Not Found"]):
                fun_not_found_case += 1
                total_case += 1
            elif (case.State == eTestCaseState["Test Successed"]):
                success_case += 1
                total_case += 1
            elif (case.State == eTestCaseState["Test Failed"]):
                fail_case += 1
                total_case += 1
            else:
                other_case += 1
                total_case += 1
                
        result += "Total Case: " + total_case.__str__() + "\n"
        result += "Succeed Case: " + success_case.__str__() + "\n"
        result += "Failed Case: " + fail_case.__str__() + "\n"
        result += "Function Not Found Case: " + fun_not_found_case.__str__() + "\n"
        result += "Other Case: " + other_case.__str__() + "\n"
        
        result += "================================\n"
        return result
    
    ''' 文件输出流程总结 '''
    def LogToFile(self):
        logfile = open(_project_root + "log/" + self.LogFileName, "w")
        logfile.write(self.TestSummarize_str())




