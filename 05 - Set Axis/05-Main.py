import numpy as np
import matplotlib.pyplot as plt


# ----------| Set Axis |----------

# Membuat data
def sinusGenerator(amplitudo, frekuensi, tAkhir, theta):
    t = np.arange(0, tAkhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t, y

t, y = sinusGenerator(1,1,4,0)


# Membuat plot
plt.plot(t,y)


# Setting axis, minimum sama maximum
plt.axis([0,4,-2,2])


# Menampilkan plot
plt.show()



'''
    NB : 
        - plt.axis() → Berfungsi untuk mensetting axis pada plot, seperti nilai minimum dan maksimum dari axis.
        - plt.axis([<xmin>, <xmax>, <ymin>, <ymax>])
        - plt.axis([0, 4, -1, 1])
    
'''

