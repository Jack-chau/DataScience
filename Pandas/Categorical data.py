'''
 Categorical data
    1. Nominal data - names
    2. Ordinal data - ordered
    3. Continous values

    Why Cateogorical data
        - save memory for repeated value
        - sorting ordinal data (lexical order might be wrong)
        - continuous values => discrete values
'''
import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import numpy as np
animals = pd.Series(['cat','dog','duck','cat','cat','bird','cat','dog'])
#print(animals)
# print(animals.unique())
# print(pd.unique(animals))
#print(animals.value_counts())
#print(pd.value_counts(animals))
df = pd.DataFrame({'animals':animals})
#print(df.animals)
#df.animals.hist()
#plt.show()
ser = df.animals.astype('category') # Cast a pandas object to a specified dtype
#print(ser)
#print(ser.values)
#print(type(ser.values)) #categorical

#print(ser.values.categories) #index
#print(ser.values.categories[:1]) #can use slicing
#print(ser.values.codes)

# change code list to values
#print(ser.values.categories.take([0,1,0,1]))
#print(ser.values.categories.take(ser.values.codes))

# specifing dtype
# animals = pd.Series(['cat','dog','duck','cat','cat','bird','cat','dog']
#                     ,dtype="category")
#print(animals)
#print(animals.values)
# df = pd.DataFrame({'animals':animals},dtype='category') # dtype=categories
# print(df.animals.values)

'''# Creation
categoryList = ['child','adult','elderly']
#categoriesIntList = [1,2,3] # category data type could be integer, floot, etc. but less meaningful

#method 1
ageGroup = pd.Categorical(categoryList)
# print(ageGroup)
ageCodes = [0,1,2,0,1,2,0,0,1,1,2]
# print(ageGroup.take(ageCodes))

# method 2
ageGroup2 = pd.Categorical.from_codes(ageCodes,categoryList)
print(ageGroup2)

ageGroupOrder = pd.Categorical.from_codes(ageCodes,categoryList, ordered=True)
print(ageGroupOrder)'''
# Column to Nominal Data
url = 'https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv'
tips = pd.read_csv(url)   # tips dataset
#print(tips.info())
#print(tips.total_bill.describe()) #min 3.07, max 50.81
#print(tips.time.value_counts())
'''Column to nominal
byteBeforeConvert = tips.time.memory_usage()
print(byteBeforeConvert)
tips['time'] = tips['time'].astype('category')
byteAfterConvert = tips['time'].memory_usage()
print(byteAfterConvert)
percentage change
print(f'Memory: {byteBeforeConvert} -> {byteAfterConvert} bytes,{byteAfterConvert/(byteBeforeConvert) *100:2f}% of original size')'''
'''# Column to Ordinal Data
#print(tips['day'].unique())
#print(tips['day'].value_counts())
byteBeforeConvert = tips.day.memory_usage()
dayCatType = pd.api.types.CategoricalDtype(categories=['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
tips['day'] = tips['day'].astype(dayCatType)
byteAfterConvert = tips.day.memory_usage()
print(f'Memory: {byteBeforeConvert} -> {byteAfterConvert} bytes,{byteAfterConvert/(byteBeforeConvert) *100:2f}% of original size')
print(tips['day'])
tips['time'] = tips.time.astype('category')
print(tips.info())
print(tips.day.cat.categories)
print(tips.day.cat.codes)
print(tips.day)
tips.day.cat.remove_unused_categories(inplace=True) #remove unuseded categories
print(tips.day)'''

# Categorical method (cat method)
#animals = pd.Series(['cat','dog','duck','cat','cat','bird','cat','dog'],dtype='category')
#print(animals.values)
#print(animals.values.categories) # unique data to categories

#add categories
#animals.cat.add_categories(['horse','tiger','zebra','lion'],inplace=True)
#print(animals.values)
#print(animals.values.categories)
#print(animals)

'''#remove categories
animals.cat.remove_categories(['cat'],inplace=True)
#print(animals)'''
'''# As ordered
animals.cat.as_ordered(inplace=True) #ordered
animals.cat.reorder_categories(['lion','tiger','horse','zebra','dog','bird','duck'],inplace=True)
animals.cat.as_unordered(inplace=True) #remove order
animals.cat.remove_unused_categories(inplace=True)
print(animals)'''

# Categorical value Ordinal Data
labels = ['cheap','normal','expensive']
#print(tips.total_bill.max()) #50.81
#print(tips.total_bill.min()) #3.07
#print(tips.total_bill.mean()) #19.7859
bins = pd.cut(tips.total_bill,3,labels=labels) #discrete intervals (cut three parts, is ordered)
#bins = pd.qcut(tips.total_bill,3,labels=labels) #discrete intervals (cut three parts, is ordered)
#bins = pd.cut(tips.total_bill,bins=[0,10,20,30]) #custom bin cut posision
#print(bins) #category datatype
#print(bins.values.codes)
#print(bins.values.categories)
#print(bins.values.describe())
#print(bins.values.describe())
#print(bins.values.value_counts())
# print(tips.total_bill.groupby(bins).agg(['count','min','max']))

'''# cut and qcut
bins = pd.cut(tips.total_bill,3) #base on 
print(bins.values.describe())
bins = pd.qcut(tips.total_bill,3)
print(bins.values.describe())'''

# Query
mask = bins.values.isin(['expensive'])
#print(mask)
#print(tips[mask]) #output true rows
#print(tips[mask])
# or
#print(tips[bins.values == 'expensive'])
#print(bins.values)
#print(tips[bins.values > 'normal'])

# sorting
#print(bins.sort_values(ascending=True))
#print(tips.sort_values(by=['day','time'],ascending=[True,True]))
dayCatType = pd.api.types.CategoricalDtype(categories=['Mon','Tue','Wed','Thur','Fri','Sat','Sun'])
tips['day'] = tips['day'].astype(dayCatType)
tips['time'] = tips.time.astype('category')
#print(tips['day'].describe())
#print(tips['time'].describe())
#print(tips.sort_values(by=['day','time'],ascending=[True,True]))
tips.total_bill[bins.values == 'cheap'].plot.hist()
plt.show()









