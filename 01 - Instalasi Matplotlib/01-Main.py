import numpy as np
import matplotlib.pyplot as plt

# Membuat lingkaran
PI = np.pi
sudut = np.linspace(0, 2*PI, 100)
radius = 5  # diameter lingkaran

x = radius * np.cos(sudut)
y = radius * np.sin(sudut)

# Inisialisasi plot
plt.plot(x, y)

# Menampilkan plot
plt.show()



'''
    NB :
        - plt.plot() → Berfungsi untuk menginisialisasi plot.
        - plt.plot(x,y)

        - plt.show() → Berfungsi untuk menampilkan plot.


'''

