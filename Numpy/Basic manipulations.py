import numpy as np
import seaborn as sns
import matplotlib.pyplot as plot
# Index & Slice
arr = np.arange(0,10) #0-9 array
# indexing[position]
#arr[0] = 999 # arr[positions to index a item and then update it
#arr[0] = 'abc' wrong, must assign same data type
#print(arr)

#slicing
#print(arr[:]) #all
#print(arr[1:3) # 1-2
#print(arr[::-1]) inverse
#print(arr[::2]) #step size 2
#view = arr[1:4]
#view[:]=[777,888,999] # will update original array
#print(arr)
# copy = arr[1:4].copy() #use .copy() to prevent overwirte
# copy[:] = [777,888,999]
# print(copy)
# print(arr)

# 2d examples
arr2d = np.arange(16).reshape(4,4)
#print(arr2d)

# indexing [row][col] OR [row,col]
#print(arr2d[0][0]) # 1st row 1st column data
#print(arr2d[1][2])  # 2nd row 3rd column data
#print(arr2d[1,2]) # 2nd row 3rd column data

# slicing[row,col]
#print(arr2d[1]) #row 1
#print(arr2d[1:3]) #row 1,2
#print(arr2d[1:3,1:3]) # 2nd-3rd row + 2nd-3rd columns

# update examples
# arr2d[1:3,1:3] = np.full([2,2],-1) #2,2 is shape , fill -1
# print(arr2d)

# increase dimension
#arr = np.arange(10)
#arr = arr[np.newaxis,:] #too 2d (add new row)
#print(arr.shape) #1row,10column
#arr = arr[:,np.newaxis] # add new column
#print(arr)
#print(arr.shape)

# Boolean Mask
animals = np.array(['cat','dog','fish','duck','cat'])
#print(np.unique(animals)) #return a boolean mask
#print(animals == 'cat') # select record
#print(animals[animals == 'cat']) # select record
np.random.seed(1)
data = np.random.randint(1,100,[5,5]) # assume this data is associated with animals
#print(data)
#print(data[animals == 'cat']) #cat in animals are 1 and 5.
#print(data[~(animals == 'cat')]) #not cat
#print(data[animals != 'cat']) # not cat
#print(data[(animals == 'cat') | (animals == 'dog')]) #Or
#print(data[(animals == 'cat') & (animals == 'dog')]) # & is and, but no this case

#print(data[data>30]) #select all items > 30
#data[data>30]= -1# assign values

# any / all function
# print((data>30).any())
# print((data>30).all())
# print((data>30).sum()) #count items >30

# Sorting
#arr = np.array([4,54,2,6,8,-1,0])
#arr = np.sort(arr)
#arr.sort()
#arr = np.sort(arr)[::-1] #reverse order

# multi dimensions
# np.random.seed(1)
# arr2d = np.random.randn(3,3)
# print(arr2d)
# arr2d = np.sort(arr2d,axis=0) #(sort by column)
# arr2d = np.sort(arr2d,axis=1) #(sort by row)
# print(arr2d)
# Fancy Index
animals = np.array(['cat','dog','fish','duck'])
#print(animals[0]) #act
#print(animals[[0,1]]) # cat, dog #pass a list as we can select multiple values
#print(animals[[-1,1]]) # cat, duck
#print(animals[[1,1,1]])

#Transpose 轉置
#arr2d = np.arange(16).reshape(4,4) #4x4 matrix
#print(arr2d)
#print(arr2d)
#print(arr2d.T) #column to row
#print(arr2d.swapaxes(0,1))

# Concatenate & Split
# arr1 = np.arange(16).reshape(2,8)
# arr2 = arr1+10
#print(arr1)
#print(arr2)
#arr3 = np.concatenate([arr1,arr2],axis=0) #vertically
#arr3 =np.vstack
#arr3 = np.row_stack([arr1,arr2])
#print(arr3)
#arr3 = np.concatenate([arr1,arr2],axis=1) #horizontally
#arr3 = np.hstack([arr1,arr2])
#arr3 = np.column_stack([arr1,arr2])
#print(arr3)
#Split array
# arrayList = np.split(arr1,[1,3,5],axis=1) #it is a list of ndarray
# print(arrayList)
#File I/O
arr = np.arange(20)
filename = "my_arr"
# save ndarray to a file
#np.save(filename,arr)

# Load ndarraay from a file
#print(np.load(f'{filename}.npy')) #add npy file extension

# compress and save multiple array to a file
# np.savez_compressed(filename,arr1=arr,arr2=np.arange(10)) #data is the key, it could be any keys (arr1,arr2)
# tmp = np.load(f'{filename}.npz') #npz file extension
# print(tmp['arr1'])
# print(tmp['arr2'])















