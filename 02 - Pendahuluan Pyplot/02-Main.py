import numpy as np
import matplotlib.pyplot as plt

# ----------| Pendahuluan Pyplot |----------

# 1. Membuat data
x = np.array([1,2,3,4,5])
y = np.array([1,4,9,16,25])
y2 = np.array([1,16,81,256,625])

# 2. Membuat plot
plt.plot(x,y)
plt.plot(x,y2)

# 3. Menampilkan plot
plt.show()



'''
    NB : 
        - Alur plotting dengan matplotlib :
            1. Membuat data
            2. Membuat plot
            3. Menampilkan plot
        - Apabila ada 2 plt.plot() maka akan plotnya akan digabung.

'''



