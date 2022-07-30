# Range Function
    # 1. Python - Range()
    # 2. Numpy - np.arange()
    # 3. Pandas
            # A. pd.date_range(start,end,periods,freq) => DatetimeIndex
            # B. pd.period_range(start, end, periods, freq) => PeriodIndex
            # C. pd.timedelta_range(start,end,period,freq) => TimedeltaIndex

#data range
import pandas as pd
import numpy as np
#print(pd.date_range('2021-10-1','2021-10-10')) # every day in range
#print(pd.date_range('2021-10-1','2021-10-10',freq='h')) # every hour in range
#print(pd.date_range('2021-10-1','2021-10-10',periods =3)) # divide into 3 sections
#print(pd.date_range('2021-10-1', periods=10, freq='d')) # start, end, periods, freq (at most 3 of them)

# period range
#print(pd.period_range('2021-10-1',periods=10)) #default frequence is day, so it is 10 days
#print(pd.period_range('2020-10-1',periods=10,freq='h'))
#print(pd.period_range('2020-10','2020-12',freq='M'))

# timedelta index
#print(pd.timedelta_range(start='1d',end='10D')) #time length is day, end with 10 days
#print(pd.timedelta_range(start='1d',periods=10,freq='2d')) #length is 1day, 10 periods with frequence 2 days for each
#print(pd.timedelta_range(start='1d 12:00:00',periods=12,freq='1h'))

'''# When you know how to create time index, you can use it to create the series
series = pd.Series(np.arange(10),index=pd.date_range('2020-10-1',periods=10))
#print(series)
series = pd.Series(np.arange(10),index=pd.period_range('2020-10-1',periods=10))
#print(series)
series = pd.Series(np.arange(10),index=pd.timedelta_range(start='1d',end='10D'))
print(series)'''

# Time in Pandas
    # 1. Timestamp -> DatetimeIndex
    # 2. Period -> PeriodIndex
    # 3. Timedelta -> TimedeltaIndex

# time = pd.Timestamp(2020,11,11)
# delta = pd.Timedelta(days=3)
#period = pd.period_range('2020', freq='A-MAR') start with march 01 - end of march
# periodMonth = pd.Period('2021-10') #create a month period
# periodDay = periodMonth.asfreq('D','s') #change to D, put it at the begining of the period

# All type of time index can be used as regular column as well, not just for index
df = pd.DataFrame({
                    'date':pd.date_range('2022-2-24',periods=10),
                    'period':pd.period_range('2021-10-1',periods=10),
                    'delta':pd.timedelta_range(start='1d',end='10D')
                  })
#print(df)

# Date query with a date variable
# deadline = pd.Timestamp.now() + pd.Timedelta(days=5)
# print(df)
# print(df.query('date> @deadline')) # use @ and add a variable

# Between date query
# fromDate = pd.Timestamp.now()
# toDate = fromDate + pd.Timedelta(days=3)
# print(df[ (df['date']>fromDate) & (df['date']<toDate) ])
# print(df.query('date>@fromDate & date<@toDate'))

# Between time query ()
dfDate = pd.DataFrame(
    {'A':[1,2,3,4,5,]},index=pd.date_range('2022-02-24',periods=5,freq='1D3H'))
#print(dfDate)
print(dfDate.between_time('9:00','18:00'))


