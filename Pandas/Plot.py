import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv'
tips = pd.read_csv(url)
labels = ['cheap','normal','expensive']
bins = pd.cut(tips.total_bill,3,labels=labels)

# matplotlib:

# tips.total_bill.plot.hist(bins=5) #bins: number of histogram bins to be used
# plt.show()

#bins.hist()
#plt.show()

# bins.value_counts().plot(kind='bar') #vertical
# plt.show()

# bins.value_counts().plot(kind='barh') #horizontal
# plt.show()

# tips.plot.scatter(x='total_bill',y='tip')
# tips.plot.scatter(y='total_bill',x='tip')
# plt.show()

'''# Using Seaborn
tips['bins'] = bins
tips['day'] = tips.day.astype('category')
#print(tips)
#count plot
#sns.countplot(x='day',data=tips) #day is categorical
sns.countplot(x='day',hue = 'size',data=tips)
plt.show()'''

# Cat polt
tips['day'] = tips.day.astype('category')
#sns.catplot(x='day',y='total_bill',data=tips)
#sns.catplot(x='day',y='total_bill',hue='sex',data=tips)
tips['bins'] = bins
#sns.catplot(x='bins',y='tip',hue='sex',data=tips)

# bar plot
# sns.catplot(x='bins',y='tip',hue='day',data=tips,kind='bar')

# box plot
# sns.catplot(x='bins',y='tip',hue='sex',kind='box',data=tips)
# plt.show()

# regrssion plot
# sns.regplot(x='total_bill',y='tip',data=tips)
# plt.show()
# pairplot

#sns.pairplot(tips,vars=['total_bill','tip'])
#sns.pairplot(tips)
#sns.pairplot(tips,kind='reg',hue='bins') #fit regrssion line
#plt.show()