import numpy as np
normal_array = np.random.normal(5, 0.5, 6) #ValueError: scale < 0
print(normal_array)	
print(np.min(normal_array))
print(np.max(normal_array))
print(np.mean(normal_array))
print(np.median(normal_array))
print(np.std(normal_array))
"""
[5.71223301 5.21000766 5.13698822 4.89204698 4.97891711 5.49562682]
4.892046975785714
5.712233009715037
5.237636633138826
5.173497944460042
0.2855001811053919
"""