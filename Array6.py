import numpy as np
a=np.arange(9)
a=a.reshape(3,3)
#a=np.split(a,3) 
print(a)
"""
[array([[0, 1, 2]]), array([[3, 4, 5]]), 
 array([[6, 7, 8]])]
"""
a=np.hsplit(a,3) 
print(a)
"""
[array([[0],
       [3],
       [6]]), array([[1],
       [4],
       [7]]), array([[2],
       [5],
       [8]])]"""
       
a=np.vsplit(a,3) 
print(a)
"""[array([[0, 1, 2]]), array([[3, 4, 5]]), array([[6, 7, 8]])]"""





















