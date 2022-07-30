import nummpy as np
# Aggregate functions
#data = np.arange(1,10)
#data = np.mean(data)
#data = np.max(data)
#data = np.min(data)
#data = np.sum(data)
#np.maximun and np.minimum is for miltiple array
#data = np.argmin(data) # index val for min item
#data = np.argmax(data)

# reduction - aggregate all values in a single array
#data = np.add.reduce(data) # add all element in array
# same as
#data = np.sum(data)

# accumulation
#data = np.add.accumulate(data) # accumulate every elements one by one
#data = np.cumsum(data)
#print(data)

'''# Commulative functions
#data = np.arange(1,10)
#data = np.cumsum(data) #accumulative sum
#data = np.cumprod(data)
data = np.array([[0,1,2,],[3,4,5],[6,7,8]])
#data = np.cumsum(data, axis=1) #add from left to right
data = np.cumsum(data,axis = 0) #add from top to down
print(data)'''
