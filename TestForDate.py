# -*-coding: utf-8 -*-
from datetime import datetime
def isrunnian(stryear):
    if stryear%400==0 or (stryear%4==0 and stryear%100!=0):
        return True
    else:
        return False


def datecount(strdate):
    count=0
    m2=0
    try:
        date_time=datetime.strptime(strdate,'%Y-%m-%d')
        strday = date_time.weekday()
        if isrunnian(date_time.year):
            m2=29
        else:
            m2=28
        for x in range(0,date_time.month):
            if x in days:
                count+=31
            elif x==2:
                count+=m2
            else:
                count+=30
        count+=date_time.day
        return count,week_day_dict[strday+1]
    except:
        return count

week_day_dict = {1 : '星期一',2 : '星期二',3 : '星期三',4 : '星期四',5 : '星期五',6 : '星期六',7 : '星期天'}


days=(1,3,5,7,8,10,12)

temp=input("输入日期：")
print (datecount(temp))

