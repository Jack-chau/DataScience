# Pandas
'''
    1. Manipulate & analyse tubular data
    2. Data structure: DataFrame & Series
'''
import pandas as pd
import numpy as np
# print(pd.__version__)
# print(np.__version__)
'''
    2 type of data structure
        a. Series: (**column**)
            - 1D-list structure
            - with index but no column
            - a column in a DataFrame
'''
# Create a Series using a list
series = pd.Series(['red','blue','green','yello'], index=['a','b','c','d'])
#print(series)
#print(type(series))
#print(series.ndim) #1d dimension
#print(series.shape) # 4 length
#print(series.size) # 4 row
#print(series.index)
#print(series.describe())
#print(series.value_counts())
#print(series[0]) #position
#print(series[:]) #slice
'''
2. DataFrame
    - 2D-table structure
    - most frequently used structure in pandas
    - with column and index
    - index could be number or string
'''
# create dataframe (using dictionary) **Row and Column
df = pd.DataFrame({'name': ['Paul','Jone','Mary','Jane'],
                   'phone':['55440772','545684','548644','6854684'],
                   'gender':['male','male','female','female'],
                    'age':[18,22,23,np.nan],
                   'series':series
                   },
                   index = ['a','b','c','d'])
#print(df)
#print(type(df))
#print(df.ndim)
#print(df.shape)
#print(df.size)
#print(df.columns)
#print(df.index)
#print(df.set_index('name')) # set name column to index, but dataframe has not changed
#df.set_index('name',inplace=True) **change original dataframe
#print(df)
#print(df.info())
#print(df.describe())
#print(df.count())
'''
# Get column in dataframe
print(df.name)  #print(dataframe column) output series
# same as:
print(df['name']) #series

# Fancy Index
# add column
#print(df[['name']]) # it is a single column DATA Frame
#print(type(df)) # is a dataframe
#print(df[['name','age']])
#print(df[['name','name']])
df['color'] = series
#print(df)
#print(df.assign(color2=series)) #does change original dataframe
df = df.assign(color2=series)
print(df)
# WARNING: to add a column, always use ['column'], instead of dot notation
'''
'''
# filter -filter (column name / index name)
#print(df.filter(items =['name'])) # or print(df.filter(['name']))
#print(df)
#print(df.filter(items=['name','age'], axis='columns')) #filter by column (dataframe)
df = df.assign(color=series)
#print(df)
#print(df.filter(like='col')) #filter as spelling
#print(df.filter(regex='r$', axis='columns')) # is a regular expression, filter r tail
#print(df.filter(regex='r$',axis = 'index'))
print(df.filter(items=['a','b'],axis = 'index')) #index
'''

'''#print(df.values) #numpy array
#print(type(df.values))
df = df.assign(color = series)
#print(df['color'][0]) #series[position]
#print(df.age.mean())
#print(df.age.median())
#print(df.age.max()) #get the maximum value
#print(df.age.idxmax()) # get maximum value and return its index
#print(df)
#df.age = df.age + 1
#print(df)
#print(df.gender.value_counts()) #group same data, data have same value
print(-(df.age)) # turn all data to negative value'''
# Update data
# df=df.assign(color2=series)
# df.color2 = 'unknow'
# print(df)
# df['color2']='_'
# df['color2'] = df['series']
# df['columnB'] = df['color2']*2 # add a column and update each item of colB
# print(df.columnB[1])
# print(df)
'''# no column name, no index name
tmpDf = df.copy() # create a new copy of dataFrame
# use fancy index to get a view of DF
tmpDf[['phone','gender']]='X' #fance index
# use Loc indexer (label based) to update data
#Syntax: df.loc[row(index),col] # Must use Label
tmpDf.loc[:,['colA','color2']] = 'red'
print(type(tmpDf.loc[:,['colA','color2']]))
#print(tmpDf)

# use iloc indexer (position based) to update data
# Syntax: df.iloc[row(index),col] #Must Use position (number)
#print(tmpDf.iloc[:,4])
tmpDf.iloc[:,4]= 'blue'
print(tmpDf)'''
# string function
#print(df.name.str.upper()) #use python string function in name column
#print(df.gender.str.count('e'))
#print(df.gender.value_counts())
#print(df.phone.str.count('^90')) # start as 90
#print(df.gender.str.len())
#print(df.name.str.split('a')) #return a series
#print(df.name.str.split('a', expand=True)) #expanded to a data frame
#print(df.name.str.contains('^p')) # start with p
#print(df.name.str.endswith('e'))
#print(df.phone.str.replace('90','Ninety')) # replace 90 as ninety
#print(df.phone.str.findall('^9'))
#print(df.phone.str.findall('\d\d\d\d')) # 4-digit group
# import re
# re.findall('^9','90909090')
# Replace data
    # 1. Series
    # 2. data frame
# series:
#print(df.name.replace('Paul','Mr,Chan',inplace = False)) #replace a string (exact match)
#print(df.name.replace('^Pa','Mr Chan',regex=True)) #regular expression, same as follow:
#print(df.name.replace(regex = "^Pa",value = 'Mr. P@')) #regular expresssion = to_replace
#print(df.name.replace(regex={'Pa':'Mr. P','ry':'rY'})) #regular expression = dict with regex & value
#print(df.gender.replace({'male':'M','female':'F'})) #replace with values in dictionary
#print(df.name.replace(['Paul','Jone'],'***')) #replace with value in list
#print(df.name.replace('a','@',regex=True)) #regular expression - series example
# same as
#print(df.name.str.replace('a','@')) #string method
#print(df['phone'])
#print(df.phone.replace(55440772,28974678)) #not work because it is object data type
#print(df.phone.astype(int).replace(55440772,28974678)) #convert it to int before replace
#print(df.age.replace(np.nan,df.age.mean())) #replace the nan number to mean value
# DataFrame
#print(df)
#print(df.replace('a','@',regex = True))
#print(df.replace(['Paul','John','male'],'*****')) #list example (for all columns)
# key of dictionary is now column name!
#print(df.replace({'name':'Paul','gender':'male'},value='xxxx')) #column:row (column name and the row data )
#print(df.replace({'name':'Paul','gender':'male'},value ='xxxx',regex=True)) #not need excet match

# Update data
#    1.apply() - series & df
#    2.applymap() -df only
#    3.map() - series only

#    1.apply()
        # for series & data frame
        # accept function

# 1) pass function
#print(df.apply(max)) #on data frame
#print(df.name.apply(len)) #apply len function on each item of this series
#print(df.age.apply(np.square)) #apply np.square function to each item of this series

# 2a) pass custom function (DF)
# def max_df(x): # x is series (each column)
#     return x.max()
# print(df.apply(max_df)) #apply on df's columns, return a series

# 2b) pass custom function (Series)
# def upper_ser(x):
#     return x.upper()
# print(df.name.apply(upper_ser)) # apply on seires's item

# 3) pass custom function (with argument)
# def upper_ser_arg(x,length):
#     return x.upper()[:length]
# print(df.name.apply(upper_ser_arg,args=(3,))) #apply on series's item (comma is required)

# 4) anoymous function
#print(df.apply(lambda x:x.max())) # on df (parameters; return)
#print(df.name.apply(lambda x:x.upper()))
#print(df.apply(max,axis='index')) #each column max

# 5) for df.apply, you can pass axis
# * 0 or 'index': apply function to each row. (vertical)
# * 1 or 'columns': apply function to each column max (horzontal)
# print(df[['age']])
# print('\n')
#print(df[['age']].apply(np.sum,axis='index')) #compute sum of each column
#print(df[['age']].apply(np.sum,axis='columns')) #by row

# result_type is only avaliable for db.apply
# result_type is for multi-value item
# expand: list-like results will be turned into columns (return dataframe if possible)
# reduce: returns a Series if possible rather than expanding list-like results, opposite of 'expand'
# broadcast: results will be broadcast to the original shape of the DataFrame, the original index

#listLikeResult = [0,1,2,3,4,5,6]
#print(df.apply(lambda x:listLikeResult, axis=1, result_type='reduce')) # return a series
#print(df.apply(lambda x:listLikeResult, axis=1, result_type='expand')) # return a DataFrame
#print(df.apply(lambda x:1, axis=1, result_type='broadcast')) # change the original data but keep the original column and row
'''# applymap()
    # data frame only
    # apply a function to every element of a DataFrame
#1) function
#print(df[['age']].applymap(np.square)) #square every element in the data frame
# 2) custom function:
def count_character(x): #x is every column
    return len(x)
print(df[['name','gender','phone']].applymap(count_character))'''
'''# map()
    #series only
    #accept dictionary or function for substitution
# 1)  substitute values using a map
#sub_dict = {'Paul':'Mr. Chan', 'Jone':'Mr. Wong'}
#print(df.name.map(sub_dict)) # will return nan if not match
#print(df.name.replace(sub_dict))

# 2) substitute values with a format
#print(df.name.map('Hello, {}'.format)) # {} like f string

# 2) substitue values with anonymous function
#print(df.name.map(lambda x:f'Hey,{x}')) # x is each item

# 3a) substitute values with a function
#print(df.age.map(np.square))

# 3b) substitute values with a function
# def change_name(name):
#     name = 'person-' + name + '-001'
#     return name
# #print(df.name.map(change_name))'''
'''# Drop a row / column
#print(df)
#print(df.drop('name',axis='columns')) # drop a row with a index value (axis = 0/ 'index', default)
#print(df.drop('d',axis='index'))'''
'''# ROW
#print(series)
#print(series[0])
#print(df[0]) # WARNING: Position is not working!!! (it's for adding col name)
# slice operation (row)
#print(df[:]) # all rows
#print(df)
#print("\n")
#print(df[:2]) # row 0 to 1
#print(df[::-1]) #reverse order'''
'''#Filter
# Axis 0: rows/index
# Axis 1: columns
# print(df.filter('a',axis='rows'))'''
'''# Indexer
    # 1. loc(label)
    # 2. iloc(position)
# 1. LOC indexer:
# SYNTAX: df.loc[row,col] # label base
# print(df.loc['a']) #get 1 row(series)
#print(df.loc[['a','b']]) #get multiple row (using fency index, pass a list inside)
#print(df.loc[:]) #get all row and columns
#print(df.loc['a':'c']) #slice (includeing c)
#print(df.loc[['a','b','c','a']]) #fency index
#print(df.loc[:,'name']) #columns
#print(df.loc[:,['name','age']])

# 2. iloc   (position base)
# SYNTAX: df.iloc[row,col]
#print(df.iloc[0]) #first row
#print(df.iloc[:]) #all row
#print(df.iloc[0:1]) #not include 1
#print(df.iloc[:,:]) #all rows, all columns
#print(df.iloc[:,0]) #all rows, first column
#print(df.iloc[:,[-1]]) #all rows, last column
#print(df.iloc[:,1]) #all rows, second column'''
'''# Boolean Mask
#mask = df.age > 20 #age series
#print(mask)
#print(~mask) #negate it
#print(df[mask]) #retrieve the results (return true result in dataframe)
#print(df[df.age>20])
#print(df.loc[mask]) #retrieve the result (iloc  not work)'''
'''# Query() like Boolean Mask, boolean mask return 0 or 1, query return your condition
#print(df.query('age==22'))
#print(df.query('age>20'))
#print(df.query('name=="Paul" & age>10'))'''
'''# Using Python str functions
#print(df.query('name.str.contains("P")',engine="python"))
#print(df.query('name.str.contains("J")', engine="python"))
#print(df.query('name.str.upper()=="PAUL"',engine='python'))
# if two condidtions, you have to add str again
#print(df.query('name.str.upper().str.contains("PAUL")',engine='python'))'''

'''# Missing Values
#print(df.age.isnull())
#print(df.age.isna())
#print(df.loc[df.age.isna()])
#print(~df.age.isnull()) #is not null
#print(df.loc[~df.age.isna()])
print(df.age.fillna(df.age.mean())) #fill the values (inplace=True if you want to save it)'''

'''# Groupby (using specific column to form a group for further process)
# *divide some data input groups (e.g.gender)
#print(df)
#print(df.groupby('gender').mean()) #group by gender, tcalculate the mean value from oher column
# same  as:
#print(df.groupby('gender').age.mean())
# same as:
#print(df.groupby('gender')['age'].mean())

# you can groupby two column
#print(df.groupby(['gender','name']).mean()) # multi-index groupby gender, then groupby name
#print(df.groupby(['gender','name']).mean().unstack()) # name to be each columns
# Pivot_table
# by default is calculate the mean
#print(df.pivot_table('age',index='gender',columns='name')) #age is data, index = gender, columns = name
#print(df.pivot_table('age',index='gender',columns='name',aggfunc='mean')) # aggfun other than mean

# Sorting
#print(df.sort_values(by='name',ascending=True))
#print(df.sort_values(by='age',ascending=False))
print(df.sort_values(by=['gender','age'],ascending=[True,False]))
#print()
# print()'''































