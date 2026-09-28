import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return np.exp(-(x**2 + y**2))

x_vals = np.linspace(-2, 2, 100) 
y_vals = np.linspace(-2, 2, 100) 

X, Y = np.meshgrid(x_vals, y_vals)

Z = f(X, Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis', alpha = 0.8)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('f(x, y)')
ax.set_title('Gaussian Surface f(x, y)')

plt.show()
