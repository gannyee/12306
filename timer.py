# coding: utf-8

#时间帮助类

from datetime import datetime, timedelta


#时间格式化 str -> date
def _date_to_str(date_time):
    return date_time.strftime('%Y-%m-%d')
	
def time_formate(date_time_str):
    date = datetime.strptime(date_time_str,'%Y-%m-%d')
    return _date_to_str(date)

now = datetime.now()

current_time = _date_to_str(now)

dateline_time = now + timedelta(days = 30) 

dateline = _date_to_str(dateline_time)

#print("current_time: " + current_time)
#print("dateline_time: " + dateline)
#print("date: " + time_formate('2019-1-1'))
