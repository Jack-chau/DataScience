'''
    Linear Algebra
        1. np.dot
        2. np.diag
        3. np.linalg.det
        4. np.linalg.eig
        5. np.linalg.inv
        6. np.linalg.solve, etc,
'''
import numpy as np
# Dot product
# a = np.array([[1,2,3],[4,5,6]]) # a is a 2x3 matrix
# b = np.array([[7,8],[9,10],[11,12]]) # b is a 3x2 matrix
# print(a.shape)
# print(b.shape)
# c = np.dot(a,b) # axb will be a 2x2 matrix
# print(c)
# determinant
# x = np.array([[6,1,1],[4,-2,5],[2,8,7]])
# np.linalg.det(x)
# print(x)

# Inverse
# np.random.seed(1)
# x = np.random.rand(3,3)
# np.linalg.inv(x)

# diagonal
# a = np.arange(9).reshape((3,3))
# np.diag(a)

'''
    slove linear matrix equations
        x + y + z = 6
        2y + 5z = -4
        2x + 5y -z =27
'''
# a = [[1,1,1],[0,2,5],[2,5,-1]]
# b = [6,-4,27]
# c = np.linalg.solve(a,b)
# print(c)
# np.random.seed(1)
# a = np.random.randn(3,3)
# b = np.random.randn(3,1)
#print(a)
#print(b)
# c = np.linalg.solve(a,b)
# d = np.linalg.inv(a).dot(b)
# print(c)
# print(d)
'''
Broadcast: vectorized opsions on arrays with different shapes
    Broadcast
        -Doing arithmetics with arrays in different shapes
'''
# Arrays with same shape -> element-wise computations
# a = np.array([1.0,2.0,3.0])
# b = np.array([2.0,2.0,2.0])
# print(a.shape)
# print(b.shape)
# c = a * b
#element-wise multiplication -> the shape of a & b are the same
# print(c)
# print(c.shape)
'''
Arrays Not in same shape
    Case 1: One of them is a scalar (number)
        1. The smaller array must stretch(拉長) to match the shape of the larger array
        2. After matching the shape -> element-wise computation

a = np.array([1.0,2.0,3.0])
b = 2 #b is a scalar
c = a*b
print(c) # since shape not match -> broadcasting (b stretch to match A - conceptually **b will not strtch in computer's memory)

 Case 2: Both of them are array but shape are different
    # RULE: In order to broadcast,
 the size of the trailing axes for both arrays in an operation must
 either be same size or one of them must be one
 example:
a = np.array([[0.0,0.0,0.0],
              [10.0,10.0,10.0],
              [20.0,20.0,20.0],
              [30.0,30.0,30.0]])
b = np.array([0,1.0,2.0])
b will be: b = np.array([[0,1.0,2.0
                         [0,1.0,2.0
                         [0,1.0,2.0
                         [0,1.0,2.0]])
c = a*b
print(c)
#################
# Broadcast rule check
################
a.shape = (4,3)
b.shape = (3,)
1x3 matrix and 4x3 matrix

    Step 1: smaller array -> append 1 on LHS (increase the dimension)
    (4,3) => (4,3) # no change
    (3,) => (1,3) # append 1 to the left
# Conclusion => compatible

step 2: stretch on All 1s to match the Larger array  
    (4,3) => (4,3) # no change
    (3,) => (1->4,3) #add 1 and stretch to 4

Step 3: if there is a match in shape, do element-wise computations with the same arrays 
(4,3)
(4,3)

###############
Incompatible: Cannot do broadcasting
##############
a = np.array([[0.0,0.0,0.0],
              [10.0,10.0,10.0],
              [20.0,20.0,20.0],
              [30.0,30.0,30.0]])  
b = np.array([0,1.0,2.0,4.0]) 

a.shape = 4x3
b.shape = 1x4
trailing axes not match, how to do?  
'''
a = np.array([0.0,10.0,20.0,30.0])
b = np.array([0.0,1.0,2.0])
#print(a.shape)
#rint(b.shape)
######add a axis behind #########
a= a[:,np.newaxis]
#print(a.shape) #now a is 4x1 matrix
c = a+b
#print(c)
'''
#####rule check######
a.shape = (4x1) -> (4x1->3) -> (4x3)
b.shape = (1x3) -> (1->4x3) -> (4x3)
'''
# In practice,
    #one of the array could be very large
    # since this process is conceptual only, it does not require so many memory in computer

np.random.seed(1)

array = np.random.random([1000,5])
mean = array.mean(axis=0) #mean for each col
print(mean.shape)
#result = array - mean
#print(result)
# 1000x5 matrix and 1x5 matrix
#match traling axis















