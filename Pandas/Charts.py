import pandas as pd
import seaborn; seaborn.set()
import mplfinance as mpf
import pandas_datareader as pdr
import matplotlib.pyplot as plt

stock = pdr.DataReader('0700.hk',start='2000',data_source='yahoo')
'''#print(stock['Volume'])
#print(stock)
#print(stock.index) #timestamp
#print(stock.loc['2020'])
#print(stock.loc['2020-1':'2020-8'])
#print(stock.Close['2020-1':'2020-8'])
#stock.Close['2020-1':'2020-8'].plot()
#plt.show()
'''
'''
# Resample based on a frequence (something like groupgby a frequence)
#series
#stock.Close.resample('W') #DatatimeIndexResampler ->do aggregate function
#print(stock.Close.resample('W').mean()) #choose close column, groupby week and calculate the mean

#print(stock.Close['2021-1'].resample('B').max()) # b is business
#print(stock.Close['2021'].resample('W').mean()) # W: week, average price of each week
#print(stock.Close['2021'].resample('Q').mean()) # Q: quarter and, average price of each quarter
#print(stock.Close['2021'].resample('M').mean()) # M month end
#print(stock.Close.resample('BA').mean().head()) #BA: business year end, average price of each year

#fig, ax = plt.subplots() # row, column (one chart)
#fig,ax = plt.subplots(2) #two row chart
#fig,ax = plt.subplots(2,2) #two row chart and 2 column chart
#plt.show()
fig,ax = plt.subplots(2)
stock.Close['2019'].resample('Q').mean().plot(ax=ax[0],style='--')
stock.Close['2019'].resample('Q').median().plot(ax=ax[0],marker='o',color='green')
stock.Close['2019'].resample('Q').min().plot(ax=ax[1],style='s',color='purple')
stock.Close['2019'].resample('Q').max().plot(ax=ax[1],style=':',color='red')
plt.show()'''
'''# Chance Frequence: asfreq() dataframe
#print(stock.asfreq('Q')) #change frequency to quarter
#print(stock.asfreq('M')) #change frequency to month, return a dataframe
#stock.asfreq('M').Close.plot(color='green',title='Change frequency plot')
# ffill = front fill, bfill = back fill
#stock.asfreq('M',method='ffill').Close.plot(color='blue',title='Change frequency plot',alpha = 0.2)
#stock.asfreq('M',method='bfill').Close.plot(color='red',marker='o',title='Change frequency plot')
#plt.show()
# print(stock.asfreq('Q')) #change frequence to quarter
# print(stock.asfreq('Q')) #change frequence to quarter'''
# Shift data:shift()
# Shift index: tshift()
#print(stock.loc['2019'].Close)
#print(stock.loc['2019'].Close.shift(2)) #shift forward, fill NaN
#print(stock.loc['2019'].Close.shift(2, fill_value='0')) #shift forward, fill NaN
#print(stock.loc['2019'].Close.shift(2, fill_value='0')) #shift forward, fill NaN
# stock.loc['2019'].Close.plot()
# stock.loc['2019'].Close.shift(30).plot(style=':',alpha = 0.4,color='green')
# stock.loc['2019'].Close.shift(-30).plot(style='--',alpha = 0.4,color='red')
# plt.show()
'''# Moving Average
stock['MA10'] = stock.Close.rolling(window=10).mean() #10 day moving average
stock['MA50'] = stock.Close.rolling(window=50).mean() #50 day moving average
stock['MA100'] = stock.Close.rolling(window=100).mean() #100 day moving average
stock['MA250'] = stock.Close.rolling(window=250).mean() #100 day moving average

stock['2020'].Close.plot()
stock['2020'].MA10.plot(style=":",color='red')
stock['2020'].MA50.plot(style=":",color='blue')
stock['2020'].MA100.plot(style=":",color='green')
stock['2020'].MA250.plot(style=":",color='purple')
plt.legend(['Close','MA10','MA50','MA100','MA250'])
plt.show()'''
'''# Bollinger Band
def bband (price,maSize,numStd):
    mean = price.rolling(window=maSize).mean()
    std = price.rolling(window=maSize).std()
    upper = mean + (std * numStd)
    lower = mean - (std * numStd)
    return mean, upper, lower

stock['MA20'], stock['Upper'], stock['Lower'] = bband(stock.Close,20,2)
stock.loc['2020':,['Close','MA20','Upper','Lower']].plot(style=['-','--',':',':',],title='Bollinger Band')
plt.fill_between(stock.loc['2020':].index,stock.loc['2020':].Upper,stock.loc['2020':].Lower,color='#E3F2FD')
plt.show()'''

# Candlestick Chart

mpf.plot(stock['2020'],type='candle',style='charles',title='Candlestick Chart',
         ylabel = 'Price (HKD)',
         ylabel_lower = 'Volume',
         volume = True,
         mav = (10,20))