'''
    pandas - Time
        1. Time API
            A. Python: datetime
            B. Numpy: datatime64 (faster)
            C. Pandas: timestamp (combine datetime & datetime64)
        2.  Time Index
            A. DatetimeIndex (Timestamp/time point)
            B. PeriodIndex (Period of time - with start time)
            C. TimedeltaIndex (Time difference - no start time)
'''
'''# Time API
#python native 
from datetime import datetime, timedelta
now = datetime.now()
#print(now)
#print(now.year)
#print(now.month)
# print(now.day)
#print(now.weekday()) #Monday is 0, sunday is 6, 0-6 7 days a week
#print(now.ctime()) # human readable
#print(now.strftime("%A, %d - %b %Y")) #string format time %A is weekday, %d is day, %b is month,Y is year
#print(datetime.strptime('Mon Sep 28 2020', "%a %b %d %Y")) # reverse of strftime
# Create datetime object
date = datetime(year=2020,month=10,day=30)
#print(date)
# add / substract a timedelta
#print(now + timedelta(days=10)) # now add 10 days
#print(now + timedelta(hours=20))
# date + now # not working! adding two data is not supported
#print(date-now) #subtraction is okey'''

'''# Numpy Time API: datetime64
import numpy as np
d = np.datetime64('2020-10-30')
#print(d)
date = np.array(['2020-10-29','2020-10-30','2020-10-31'],dtype=np.datetime64)
#print(date)
#print(date[2])
#datalist = date + 10 #each elements in array add 10
#print(datalist)
list = np.arange(100) #array
#print(list)
print(list + date[0])'''
# Pandas Time API: timestamp (python.datetime + numpy.datetime64)
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

'''ts = pd.to_datetime("31 Oct 2020")
#print(ts)
# print(ts + pd.Timedelta(days=1))
# print(ts.year)
# print(ts.month)
# print(ts.weekday())
# print(ts.strftime("%A %d - %b %Y"))

# time delta index (Time difference, no start time)
delta = pd.to_timedelta(np.arange(10),'h') #create 10 timedelta in hours
#print(delta)
#print(ts + delta) # a timestamp + a timedelta return a DatatimeIndex
# warning: you cannot just add an integer to a timestamp or timestamp array
#ts +1 #did not work because timestaeam cann't add an integer'''

# Createing Index
    # DatetimeIndex => pd.DatetimeIndex([...]) OR pd.datetime([...]) =>index with ts vallues
    # PeriodIndex => datetimeIndex.to_period([...])
    # TimedeltaIndex => pd.TimedeltaIndex([...]) OR datetimeindex-datetimeindex =>index with timedelta value

#dateTimeIndex = pd.DatetimeIndex(['2020-10-01','2020-10-02','2020-11-01','2020-11-02','2021-11-01','2021-11-1'])
# is a timesteam
#print(index)
#print(index - pd.Timedelta(days=2)) #timesteam can - timedelta
# method 2) use pd.to_datetime()
#dateTimeIndex = pd.to_datetime([datetime(2020,10,1),datetime(2020,10,2),datetime(2020,11,1),
#                        '2020-11-02','2021-10-01','2022-10-01'])
#python datetime(xxxx,xx,x)
#print(index)
#ser = pd.Series([1,2,3,4,5,6],index=dateTimeIndex)
#print(ser)

#Filter
#print(ser['2020']) #filter by year
# print(ser['2020-10']) #filter by month
#print(ser['2020':'2021']) #slice by year
#print(ser['2020-01-01':'2021-10-1']) #slice by date
# print()

#PeriodIndex
datetimeIndex = pd.DatetimeIndex(['2020-10-01','2020-10-02','2020-11-01','2020-11-02','2021-11-01','2021-11-1'])
#print(datetimeIndex) #dtype is datetime64[ns]

#convert a DateTimeIndex to PeriodIndex
#print(datetimeIndex.to_period('D')) #period is a period of time, with start time, D is day and the period

# Time DeltaIndex
#print(datetimeIndex - datetimeIndex) #return datetimeIndex
#print(datetimeIndex - datetimeIndex[0]) #return datetimeIndex
#print(datetimeIndex + pd.Timedelta(days=1)) #return datetimeIndex

#Or
timedeltaIndex = pd.TimedeltaIndex([pd.Timedelta(days=1),pd.Timedelta(days=2),pd.Timedelta(days=3)])
print(timedeltaIndex)








