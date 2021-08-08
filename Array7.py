import numpy as np
a=np.arange(9)  
a=a.reshape(3,3)
s=np.resize(a,(3,2))
print(s)
"""
[[0 1]
 [2 3]
 [4 5]] """
a=np.append(a, [9,-10,11])
print(a[-1])

"""
s=np.insert(s, 2, [5,5,5])
print(s)

s=np.delete(s,5)
print(s)

s=np.delete(s,np.s_[2:5]) #2 to 3
print(s)
"""

"""
[[0 1]
 [2 3]
 [4 5]]
[ 0  1  2  3  4  5  6  7  8  9 10 11]
[0 1 5 5 5 2 3 4 5]
[0 1 5 5 5 3 4 5]
[0 1 3 4 5]
"""






