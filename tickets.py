#coding: utf-8

"""
命令行火车票查看器

Usage:
    tickes [-gdtkz] <from> <to> <date>


Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""

import requests

import sys

from docopt import docopt

from stations import stations, station_english_to_chinese

from prettytable import PrettyTable

from colorama import init, Fore

from timer import current_time,dateline,time_formate
init()

def cli():
    "command-linr interface"

    arguments = docopt(__doc__)

    from_station = stations.get(arguments['<from>'])

    to_station = stations.get(arguments['<to>'])
    
	#格式化输入时间
    date = time_formate(arguments['<date>'])

    if date < current_time:
        print("只能查询时间起始于：" + current_time + " 的班次信息")
        sys.exit()
    elif date > dateline:
        print("只能查询时间截止于：" + dateline + " 的班次信息")	
        sys.exit()
		
    #print(arguments)
    
    # 构建URL
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)

    #print("url: " + url)

    # 获取参数
    options = ''.join([
    
        key for key, value in arguments.items() if value is True
        
    ])
    
    
    # 添加verify=False 参数不验证证书

    r = requests.get(url,verify=False) 

    available_trains = r.json()['data']['result']
    
    #print(r.json()['data']['result'])
    TrainsCollection(available_trains,options).pretty_print()
    
class TrainsCollection:
    
    header = '车次  车站  时间  历时  一等  二等  软卧  硬卧  硬座  无座'.split()
    
    def __init__(self, available_trains, options):
        """查询到的火车班次集合
           
          :param available_trains:一个列表，包含可获得的火车班次，每个火车班次是一个字典
          
          :param options:查询的选项，如高铁，动车，etx....
          
        """

        self.available_trains = available_trains
        self.options = options
        
    def _get_duration(self,train_array):
        duration = train_array[10].replace(':','小时') + '分'
        
        if duration.startswith('00'):
            return duration[4:]
            
        if duration.startswith('0'):
            return duration[1:]
        
        return duration
        
    @property
    def trains(self):
        for raw_train in self.available_trains:
            train_array = raw_train.split('|')
            train_no = train_array[3] #班次
			
			
            if(not self.options or train_no[0].lower() in self.options ):
                train = [
                train_no, 
                '\n'.join([Fore.GREEN + station_english_to_chinese.get(train_array[4] ) + Fore.RESET,
			    Fore.RED + station_english_to_chinese.get(train_array[5]) + Fore.RESET]), # 始发站和终点站
                '\n'.join([Fore.GREEN + train_array[8] + Fore.RESET,Fore.RED + train_array[9] + Fore.RESET]), # 发车时间和达到时间
                self._get_duration(train_array), # 途经时间
                train_array[31], # 一等座
                train_array[30], # 二等座
                train_array[23], # 软卧
                train_array[28], # 硬卧
                train_array[29], # 硬座
                train_array[26], # 无座
            
                ]
            
                yield train
            
    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        
        for train in self.trains:
            pt.add_row(train)
        
        print(pt)
        
if __name__=='__main__':
    cli()
