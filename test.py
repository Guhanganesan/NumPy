import numpy as np

a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2) 
print(b)

b = a.reshape(2,2,3)  #3 dimensions
print(b)

