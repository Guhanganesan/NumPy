import numpy as np
# create 2x2 matrix
a = np.matrix([[1, 2], [3, 4]])  # using array of array
print('2x2 matrix is:\n', a)

print('The dimension of the matrix is :', a.shape)

# using MatLab syntax in string
b = np.matrix('[1,2;3,4;5,6]', dtype=np.int32)  
print('\n3x2 matrix is:\n', b)

print('The dimension of the matrix is :', b.shape)

# using numpy.random.rand(row, column)
c = np.matrix(np.random.rand(3, 3), dtype=np.float32)  
print('\n3x3 random element matrix is:\n', c)

print('The dimension of the matrix is :', c.shape)
