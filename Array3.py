import numpy as np

a=np.array([
    [1,2,3],
    [4,5,6]
])
print(a.size) #6
print(a.shape) #rows,cols (2,3)
print(a.dtype) #int32
print(a.ndim) #no of rows 2
print(a.flatten()) #sinlge dimensional array
                   #[1 2 3 4 5 6]


a=np.arange(12) 
print(a) #[ 0  1  2  3  4  5  6  7  8  9 10 11]
a=a.reshape(3,4)
print(a)
"""
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
 """
a=a.reshape(2,2,3) #dim, rows, cols
print(a)
"""
[[ 6  7  8]
  [ 9 10 11]]]
"""
x = np.array([[1, 2], [3, 4], [5, 6]]) 
y = x[[0,1,2], [0,1,0]] #0->[1,2], 1->[3,4], 2->[5,6]
print(y)  #[1 4 5]


