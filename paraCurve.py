import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 2 * np.pi, 200)
x = np.sin(2 * t)
y = np.cos(3 * t)
z = x * y

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='f(x, y) = xy, x = sin(2t), y = cos(3t)')

ax.set_xlabel('x = sin(2t)')
ax.set_ylabel('y = cos(3t)')
ax.set_zlabel('')

ax.set_title('3D Plot of the Curve f(x, y) = xy')

ax.legend()

plt.show()