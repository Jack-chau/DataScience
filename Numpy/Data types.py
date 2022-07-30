import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
'''Data types (dtype)
    - some facts:
        1 byte = 8 bits
        signed -> positive, negative,0
        unsigned -> positive,0
    - Type codes for the following types:
        1. int
        2. float
        3.bool
        4.object
        5.string
        6. unicode
Type code
    1) integer
        i1 -> signed 8bit int, Type: int8 (i1 = 1 byte), i1 is type code
        i2 -> signed 16bit int, Type: int16 (i2 = 2 byte) i2 is type code
        i4 -> signed 32bit int, Type: int32 (i3 = 3 byte) i3 is type code
        i8 -> signed 64bit int, Type: int64 (i4 = 4 byte) i4 is type code

    u1,u2,u4,u8 -> unsigned int (uintX)

    2) float
        f2 -> 16 bit floating point, Type: float16
        f4 -> 32 bit floating point, Type: float32
        f8 -> 64 bit floating point, Type: float64

    3) bool
        ? -> True or False

    4) object
        O -> python object, type: object

    5) string
        S -> Fixed-length ASCII char, S4 -> 4 ASCII characters, Type: string_

    6) unicode
        U -> Fixed-Length Unicode, Type:unicode_
'''
#int16_i2 = np.dtype('i2')
# print(int16_i2)
# print(int16_i2.byteorder)
# data = np.array([0,-1,2,3,4],dtype=int16_i2) #set datatype to int_16
# or
# data = np.array([0,-1,2,3,4], dtype=np.int16)
# print(data)
'''# Create array using np data types (not type code here)
#data = np.arange(0,10,dtype=np.int8)  # 8bit integer
#data = np.arange(0,10,dtype=np.int16)  # 16bit integer
#data = np.arange(0,10,dtype=np.float64)  # 64bit floating point
# data = np.array([0,-1,2,3,4],dtype=np.bool_)  # zero is False, non-zero is True
#data = np.array([0,-1,2,3,4,99999999], dtype=np.string_) #fixed length string, b: byte
#print(data)
#print(data.dtype)
# Byte order
# (>) big-endian (Low to High)
# (<) little-ending (high to low)
# (|) not applicable
# Changing array dtype after creation
data = np.array([0,-1,2,3,4,11112222],dtype=np.string_)
#print(data.dtype) # is a S8 string
data = data.astype(bool) # use astype to change data type
# or 
# data = data.astype('?') change to bool
# data = data.astype('i2') 16 bit integer
print(data)
print(data.dtype)
'''
# Universal Function (U function): vectorized ops
'''# Vectorized Computations
#data =np.arange(1,11,dtype=np.int16) #16bit integer

# addition
# data += data
# np.add(data,data)
# print(data)
# print(data.shape)
# print(data.size)

# Subtraction
#data = data -1
#data = np.subtract(data,1)
#print(data)

# multiply
#data = data *2
#data = np.multiply(data,2)
#print(data)

# divide
# data = np.divide(1,data) #(1/data)

# squar
# data = data**2
# np.square(1,data)'''
'''
Universal Function (ufunc)
    - perform element-wise operations on ndarray (pair each element in different array)
    - vectorized computations listed above are all ufuncs   
    - Some ufuncs:
        1.np.add, np.subtract, np.negative
        2.np.multiply, np.divide
        3.np.power 
        4.np.mod
        5.np.maximum, np.minimum
        6. np.square, np.sqrt
        7. np.exp
        8. np.log, np.log10, np.log2, np.log1p
        9. np.isnan
        10.np.sin,np.cos,np.tan
        11.np. greater, np.greater_equal
'''
'''
arr1 = np.array([-1,2,3,4,5])
arr2 = np.array([2,0,7,-1,8])
data = np.maximum(arr1,arr2)
#print(data)
#print(np.abs(arr1)) #absulute values
#arr1 = np.abs(arr1)
#print(arr1)
#print(np.sqrt(arr1))
x = np.arange(0,10,step=0.1)
s = np.sin(x)
c = np.cos(x)
plt.grid(True)
plt.plot(x,s) #sin
plt.plot(x,c) # cos
plt.legend(['Sin(x)','Sin(x)'])
plt.title('Sin & Con Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(color='black')
plt.show()
# greater than
arr1 = np.array([1,2,3,4,5])
print(arr1 > 3) #return bool
print(np.greater(arr1,3))
'''




