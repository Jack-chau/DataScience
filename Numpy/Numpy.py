'''
NumPy
    1. Array creation & data types
    2. Universal function: vectorized ops
    3. Basic manipulation: indexing, slicing, boolean mask, fency index, etc.
    4. Broadcast: vectorized ops on arrays with different shapes
Why numpy array?
    -Array: collection of items, with the same data type
            - Saving computational time and memory space
                - Python list is slower and take up more space
            - Vectorized popular, data exchange for different package
            - Extremely popular, data exchange for different package
            - Linear algebra operations
'''
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
'''print(np.__version__)
print(pd.__version__)
print(plt.__version__)
print(sns.__version__)'''
'''# 1) Array creation & data types
 # Basic OPerations
 
 # 1d array
data = np.arange(1000)
#print(type(data))
#print(data.ndim) # check dimensions
#print(data.shape) #Lengh
#print(data.dtype) #same dtype in a array 32bit integer
print(data.strides) #步長 -> skip 4 byte to next item in this dimension
# (32 bit / 8 to byte), 4 byte for a data'''

'''# 2d array
np.random.seed(1) #make sure we saw the same random value when we run the task every times
data = np.random.randn(2,3) #2row x 3 columns
#print(data)
#print(data.ndim) # two dimensions
#print(data.dtype) # float64
#print(len(data))
#print(data.strides) # 24 byte in a row, 8 byte in a column
np.set_printoptions(precision=8,suppress=True) # 2 decimal point (suppression true, fixed point notation)
#pandas based on numpy
#data.to_numpy() #convery data to numpy '''
'''# Creating ndarray
    1. np.array()
    2. np.arange()
    3. no.zeros()
    4.np.ones(0
    5.np.empty()
    6. np.full()
    7. np.eye() / np.identity()
    8. np.random.random() / np.random.randint()
    9. np.linspace()
'''
'''# method 1: List
# data = np.array([[1,2],[3,4],])
# print(data.ndim)

# method 2: np.arange(start,stop,step,dtype)
#data = np.arange(10,100,3,dtype='float')
# data = np.arange(100).reshape(10,10) # reshape() to change the shape
# print(data)
#print(data.ndim)

# method 3: np.zeros()
#data = np.zeros(5)
#data = np.zeros((2,3))
# data = np.zeros([2,3])
# print(data)

# method 4: np.ones()
#data = np.ones(5)
#data = np.ones([2,3])
#print(data)

# method 5: np.empty() # no init, but faster (random data)
#data = np.empty(10)
#print(data)

# # method 6: np.full(shape, fill_value)
# data = np.full([2,3],9.9) # create a 2 x 3 array, fill all 9.9
# print(data)

# method 7: np.eye(N)/ np.identity(N) # identical matrix
# data = np.eye(5,3)  #can use dimensions
# print(data)
# data = np.identity(5) #only one dimensions
# print(data)
# method 8: np.random.random(shape) #generate random array
# data = np.random.random([3,3])
# print(data)

# method 9: np.random.randint(low,high,shape)
#np.random.seed(1) # set random run samilar
# data = np.random.randint(0,100,[3,3]) #from 0-100, 3 x 3 matrix
# print(data)

# method 10: np.linspace(start,stop,num) #From 0-1, equal separated to 10
# data = np.linspace(0,1,10)
# print(data)'''

















