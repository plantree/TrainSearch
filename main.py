#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Command line train ticket viewer

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h, --help show help menu
    -g         high-speed rail
    -d         EMU
    -t         faster rail
    -k         fast rail
    -z         straight rail

Example:
    tickets 北京 上海 2017-12-18
    tickets -dg 成都 南京 2017-12-18


Created on 2017/12/18 15:34

@author: Lucifer
@site: plantree.me
@email: wpy1174555847@outlook.com

"""

#from docopt import docopt
from utils import *


if __name__ == '__main__':
    """command-line interface"""
    #options = docopt(__doc__)
    #TrainsSearch(options).pretty_output()
        while True:
        fromStation = input('From: ')
        toStaion = input('To: ')
        date = input('Date: ')
        kinds = input('Option: ')
        print('Please wait for a moment...')
        options = {'<from>': fromStation, '<to>': toStaion, '<date>': date}
        if kinds == False:
            for kind in ('G', 'D', 'T', 'K', 'Z'):
                options['-' + kind] = True
        else:
            kinds = kinds.upper()
            for kind in ('G', 'D', 'T', 'K', 'Z'):
                if kind in kinds:
                    options['-' + kind] = True
                else:
                    options['-' + kind] = False

        TrainsSearch(options).pretty_output()
        choice = input('Continue?(y/n)')
        if choice.lower() == 'n':
            break