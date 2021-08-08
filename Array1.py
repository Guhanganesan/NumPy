#python -m pip install --upgrade pip
#pip install numpy

#Array and its methods

import numpy as np 
a = np.array([[1,2,3,7]]) 
#print(a.shape)

#(2,4)

a = np.array([[1,2,3],[4,5,6]]) 
a.shape = (3,2) 
#print(a)
"""
[[1 2]
 [3 4]
 [5 6]]
 """

a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2) 
#print(b)

"""
[[1 2]
 [3 4]
 [5 6]]
"""
import numpy as np 
#sudo apt install python-numpy
a = np.arange(24) 
#print(a)
# [ 0  1  2  3.......18 19 20 21 22 23]

a = np.arange(24) 
#print(a.ndim)  #1



b = a.reshape(2,4,3)  #3 dimensions
#print(b)

x = np.zeros((5,), dtype = np.int) 
#print(x) #default dtype is float


x = np.zeros((2,2), dtype = [('x', int), ('y', int)])  
#print(x)
"""
[[(0, 0) (0, 0)]
 [(0, 0) (0, 0)]]
"""

x = np.ones(5, dtype=int) 
#print(x)
"""[1 1 1 1 1] """



#convert list into array
x = [1,2,3] 
a = np.asarray(x) 
#print(a)
"""[1 2 3]"""

# use iterator to create ndarray 
list = range(5) 
it = iter(list)
x = np.fromiter(it, dtype = float) 
print(x)  
"""[0. 1. 2. 3. 4.]"""

