import sys
from os import path
import threading
sys.path.append(path.join(path.dirname(__file__), '..'))

from target.pyctpmd import MdApi
from datetime import datetime

class MhMdApi(MdApi):

    def __init__(self):
        print("start to initialize...")
        super().__init__()
        pass

    def onFrontConnected(self):
        print("my  onFrontConnected!")
        # loginfield ={'BrokerID':'16363','UserID':'802274','Password':'minghong123'}
        loginfield ={'BrokerID':'999','UserID':'1787','Password':'123456'}
        rt = md.reqUserLogin(loginfield,0)
        if(rt == 0):
            print("md 登入请求发送成功")
        else:
            print(f"md 登入请求发送失败，错误代码'{rt}'")
    
    def onRspUserLogin(self, data, error, task_id, is_last):
        print("my OnRspUserLogin ")
        print(self.subscribeMarketData("m2201"))
        print(self.subscribeMarketData("m2203"))
        print(self.subscribeMarketData("m2205"))

    def onRspSubMarketData(self, data, error, reqid, is_last):
        print(data)
        print(error)
    
    def onRtnDepthMarketData(self, data):
        print(f"{data['InstrumentID']}, {data['LastPrice']}")
        # print(f"{datetime.now()}")

md = MhMdApi()
md.createFtdcMdApi('../target/')

# openctp 7x24
# md.registerFront('tcp://122.51.136.165:20004')

# simnow 7x24
md.registerFront('tcp://180.168.146.187:10131')

# 实盘
# md.registerFront('tcp://180.168.102.233:41168')
md.init()

print('inited')
while True:
    pass