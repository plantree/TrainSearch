#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2017/12/18 16:07

@author: Lucifer
@site: plantree.me
@email: wpy1174555847@outlook.com
"""

from bs4 import BeautifulSoup
from colorama import init, Fore
from datetime import datetime
import pandas as pd
from prettytable import PrettyTable
from pprint import pprint
from pypinyin import lazy_pinyin
import re
from selenium import webdriver
import time
from utils import *


class TrainsSearch:

    header = '车次 车站 时间 历时 商务座 一等座 二等座 软卧 硬卧 硬座 无座'.split()

    def __init__(self, options):
        self.trains = []
        self.options = options
        self.search()


    def search(self):
        from_station = ''.join(lazy_pinyin(self.options.get('<from>')))
        to_station = ''.join(lazy_pinyin(self.options.get('<to>')))
        date = self.options.get('<date>')
        curDate = datetime.now().date()
        days = (pd.to_datetime(date) - pd.to_datetime(curDate)).days + 1
        if days <= 0:
            return
        else:
            url = 'http://trains.ctrip.com/TrainBooking/Search.aspx?from={}&to={}&day={}&' \
                .format(from_station, to_station, days)
            driver = webdriver.PhantomJS()
            driver.get(url)
            time.sleep(3)
            html = driver.page_source
            self.parse_html(html)


    def parse_html(self, html):
        bsObj = BeautifulSoup(html, 'lxml')
        searchList = bsObj.find('div', {'id': 'searchlsit'})
        items = searchList.find_all('div', {'class': 'tbody'})

        for item in items:

            train = {}
            # train's name
            name = re.split('\s+', item.find('div', {'class': 'w1'}).get_text().strip())[0]

            # time of from and arrive
            timeList = re.split('\s+', item.find('div', {'class': 'w2'}).get_text().strip())
            if len(timeList) == 2:
                fromTime, toTime = timeList
            elif len(timeList) == 3:
                fromTime, toTime, other = timeList
                toTime += ' ' + other

            # stations of from and arrive
            _, fromStation, _, toStation = re.split('\s+', item.find('div', {'class': 'w3'}).get_text().strip())
            passTime = item.find('div', {'class': 'w4'}).get_text().strip()

            train = {'name': name, 'fromTime': fromTime, 'toTime': toTime, 'fromStation': fromStation,
                     'toStation': toStation, 'passTime': passTime}

            # info about seat, price and left tickets
            seatList = item.find('div', {'class': 'w5'}).find_all('div', {'seat': re.compile('.*')})
            for seat in seatList:
                seatName = seat.find('span').get_text().replace(' ', '').replace('\t', '')\
                            .replace('\n', '').replace('\u3000', '')
                price = seat.find('b').get_text().replace(' ', '').replace('\t', '').replace('\n', '')
                tickets = seat.find('strong').get_text().replace(' ', '').replace('\t', '').replace('\n', '')
                train[seatName] = '¥' + price + '/' + tickets

            self.trains.append(train)

    def pretty_output(self):

        # colorama init
        init()

        header = '车次 车站 时间 历时 商务座 一等座 二等座 软卧 硬卧 硬座 无座'.split()
        trains = self.trains
        options = self.options
        trainType = [x.upper()[1] for x in options if options[x] == True]
        if len(trainType) == 0:
            trainType = ['G', 'D', 'T', 'K', 'Z']
        pt = PrettyTable(header)
        for train  in trains:
            name = train.get('name')
            if name[0] in trainType:
                firstLine =[]
                firstLine.append(train.get('name'))
                firstLine.append(Fore.GREEN + train.get('fromStation') + Fore.RESET)
                firstLine.append(train.get('fromTime'))
                firstLine.append(train.get('passTime'))
                for seat in '商务座 一等座 二等座 软卧 硬卧 硬座 无座'.split():
                    firstLine.append(train.get(seat, '--'))

                secondLine = ['' for i in range(11)]
                secondLine[1] = Fore.RED + train.get('toStation') + Fore.RESET
                secondLine[2] = train.get('toTime')
                pt.add_row(firstLine)
                pt.add_row(secondLine)
        print(pt)

