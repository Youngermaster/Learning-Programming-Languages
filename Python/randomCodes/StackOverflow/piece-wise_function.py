import numpy as np
import matplotlib.pyplot as plt 

def fun (n, x): 
    if n <= x <= n + 1:
        return float(x) - n 
    elif n + 1 <= x <= n + 2:
        return 2.0 - x + n 
    return 0.0 

vfun = np.vectorize(fun)

x = np.linspace(0, 10, 1000)    
y = vfun(3, x)

plt.plot(x, y, '-')
plt.show()
