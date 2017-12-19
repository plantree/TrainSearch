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

from docopt import docopt
from utils import *


if __name__ == '__main__':
    '''
    f = open('../上海到北京火车票网上订票_火车票价预订查询【携程火车票预订】.html', 'r')
    html = f.read()
    trains = parse_html(html)
    pretty_output(trains)
    '''
    """command-line interface"""
    arguments = docopt(__doc__)
    TrainsSearch(arguments).pretty_output()
