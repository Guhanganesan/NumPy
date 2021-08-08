import numpy as np 
"""
print(np.pi)
print(np.sin(90))
val=(np.pi/180)*90
print(np.sin(val))

3.141592653589793
0.8939966636005579
1.0

val=(np.pi/180)*90
sinval=np.sin(val)
inv=np.arcsin(sinval)
deg=np.degrees(inv)
print(deg)

90.0
"""


"""
print(np.around(23.6778))
print(np.around(23.6778,1))
print(np.around(23.6778,-1))
print(np.around(23.6778,2))
print(np.floor(25.7889))
print(np.ceil(25.7889))
24.0
23.7
20.0
23.68
25.0
26.0
"""
print(np.add(10,20))
print(np.subtract(10,20))
print(np.multiply(10,20))
print(np.divide(10,20))
print(np.power(10,2))
print(np.mod(11,2))
"""
30
-10
200
0.5
100
1
"""



print(np.real(11+6j))
print(np.imag(11-6j))
print(np.conj(11+2j))
print(np.angle(11+2j))
print(np.angle(11+2j, deg=True))
"""
11.0
-6.0
(11-2j)
0.17985349979247828
10.304846468766033
"""


