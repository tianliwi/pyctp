# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), '..'))

from target.pyctptd import TdApi
from datetime import datetime
from json import dumps
from time import sleep

class MhTdApi(TdApi):

    def __init__(self):

        print("Starting td...")
        super().__init__()

        self.connected = False
        self.logged_in = False

        self.req_id = 0
    
    def onFrontConnected(self):

        print("Connected")
        self.connected = True
        # auth_field = {
        #     'AppID': 'client_mnghong_1.0',
        #     'AuthCode': 'FLXALDKJOV3Q6PA3',
        #     'BrokerID': '16363',
        #     'UserID': '8020762' 
        # }
        auth_field = {
            'AppID': 'simnow_client_test',
            'AuthCode': 'MDAwMDAwMDAwMDAwMDAwMA==',
            'BrokerID': '999',
            'UserID': '1787' 
        }
        rt = self.reqAuthenticate(auth_field, self.req_id)
        print(rt)
        self.req_id += 1

    def onRspAuthenticate(
        self,
        pRspAuthenticateField: dict,
        CThostFtdcRspInfoField: dict,
        nRequestID: int,
        bIsLast: bool
    ):

        print("Auth'ed")
        # login_field = {
        #     'BrokerID': '16363',
        #     'UserID': '8020762',
        #     'Password': 'minghong123'
        # }
        login_field = {
            'BrokerID': '999',
            'UserID': '1787',
            'Password': '123456'
        }
        self.reqUserLogin(login_field, self.req_id)
        self.req_id += 1
    
    def onRspUserLogin(
        self,
        pRspUserLogin: dict,
        pRspInfo: dict,
        nRequestID: int,
        bIsLast: bool
    ):
        print("Logged in")
        self.logged_in = True

        print(pRspUserLogin)
        print(f"max order ref: {pRspUserLogin['MaxOrderRef']}")

        order_ref = 100 # int(pRspUserLogin['MaxOrderRef'])

        # self.queryOrder()

        # sleep(1.5)

        # self.queryPosition()

        order_req = {
            'BrokerID': '999',
            'InvestorID': '1787',
            'OrderRef': str(order_ref).ljust(12),
            'UserID': '1787',
            'OrderPriceType': '2',
            'Direction': '0',
            'CombOffsetFlag': '0',
            'CombHedgeFlag': '1',
            'LimitPrice': 3255,
            'VolumeTotalOriginal': 1,
            'TimeCondition': '3',
            'VolumeCondition': '1',
            'MinVolume': 1,
            'ContingentCondition': '1',
            'StopPrice': 0,
            'ForceCloseReason': '0',
            'InstrumentID': 'm2205',
            'IsAutoSuspend': 0,
            'ExchangeID': 'DCE'
        }
        rt = self.reqOrderInsert(order_req, self.req_id)
        self.req_id += 1
        print(f'sent order, {rt}')

    def onRspQryOrder(
        self,
        pOrder: dict,
        pRspInfo: dict,
        nRequestID: int,
        bIsLast: bool
    ):
        print(pOrder)

    def onRspQryInvestorPosition(
        self,
        pInvestorPosition: dict,
        pRspInfo: dict,
        nRequestID: int,
        bIsLast: bool
    ):
        print(pInvestorPosition)

    def onRspOrderInsert(
        self,
        pInputOrder: dict,
        pRspInfo: dict,
        nRequestID: int,
        bIsLast: bool
    ):
        print(f"onRspOrderInsert: {pInputOrder}")

    def onRtnOrder(self, pOrder: dict):
        print(pOrder)

    def onRspError(self, pRspInfo, nRequestID, bIsLast):
        print(pRspInfo)

    def queryOrder(self):
        qry_field = {
            'BrokerID': '999',
            'InvestorID': '1787'
        }
        rt = self.reqQryOrder(qry_field, self.req_id)
        self.req_id += 1

        if rt == 0:
            print("query order succeed.")
        else:
            print(f"query order failed: {rt}")

    def queryPosition(self):        
        # position_field = {
        #     'BrokerID': '16363',
        #     'InvestorID': '8020762'
        # }
        position_field = {
            'BrokerID': '999',
            'InvestorID': '1787'
        }
        rt = self.reqQryInvestorPosition(position_field, self.req_id)
        self.req_id += 1

        if rt == 0:
            print("query position succeed.")
        else:
            print(f"query position failed: {rt}")

td = MhTdApi()
td.createFtdcTraderApi('../target')
# td.registerFront('tcp://180.168.146.187:10130')
td.registerFront('tcp://122.51.136.165:20002')
td.init()

while True:
    pass