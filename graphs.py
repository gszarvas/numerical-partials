### Rise / Run Graph ###

# import numpy as np
# import matplotlib.pyplot as plt

# def f(x):
#     return x**2

# def secant_line(x, h=1):
#     return 1 + (x - 1) * (f(1 + h) - f(1)) / h

# x_vals = np.linspace(0, 3, 400)
# y_vals_f = f(x_vals)  # Function values f(x)
# y_vals_secant = secant_line(x_vals) 

# x_vals_run = np.linspace(1, 2, 100) 
# y_vals_run = np.linspace(1, 1, 100)

# plt.plot(x_vals, y_vals_f, label="f(x) = x^2", color='r')

# plt.plot(x_vals, y_vals_secant, label="Secant line", color='b')

# plt.plot(x_vals_run, y_vals_run, label="Run", color='k')

# # A vertical line at x = 2 from y = 1 to y = 4
# x_rise = np.full_like(np.linspace(1, 4, 100), 2)
# y_rise = np.linspace(1, 4, 100) 
# plt.plot(x_rise, y_rise, label="Rise", color='black')

# plt.xlim(0, 3)
# plt.ylim(0, 5)
# plt.xlabel("x")
# plt.ylabel("y")

# plt.text(1.5, 0.75, 'Run', fontsize=12, color='black', verticalalignment='center', horizontalalignment='center')

# plt.text(2.2, 2.5, 'Rise', fontsize=12, color='black', verticalalignment='center', horizontalalignment='center')

# plt.show()


### Joint CDF Graph ### 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function f(x, y)
def f(x, y):
    return (1 - np.exp(-x)) * (1 - np.exp(-y))

# Create x and y values for the plot
x_vals = np.linspace(0, 5, 150)  # x values between 0 and 5
y_vals = np.linspace(0, 5, 150)  # y values between 0 and 5

# Create a meshgrid for the x and y values
X, Y = np.meshgrid(x_vals, y_vals)

# Calculate the corresponding f(x, y) values
Z = f(X, Y)

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis', alpha = 0.8)

# x_fixed = 1
# y_vals_line = np.linspace(0, 5, 150)  # Same y range
# z_vals_line = f(x_fixed, y_vals_line)  # Compute z for fixed x = 1

y_fixed = 1
x_vals_line = np.linspace(0, 5, 150)  # Same y range
z_vals_line = f(x_vals_line, y_fixed)  # Compute z for fixed y = 1

ax.plot(x_vals_line, np.full_like(x_vals_line, y_fixed), z_vals_line, color='#000000', linewidth=3, label="y = 1 line")

# # Directional Derivative
# start_point = np.array([1, 2])
# direction = np.array([1, 1])
# line_length = 2
# slope = 0.2854 

# direction_normalized = direction / np.linalg.norm(direction)

# z_start = f(start_point[0], start_point[1])

# x_vals_line = np.linspace(start_point[0], start_point[0] + line_length * direction_normalized[0], 2)
# y_vals_line = np.linspace(start_point[1], start_point[1] + line_length * direction_normalized[1], 2)

# ## TANGENT LINE ###
# z_vals_line = z_start + slope * np.linspace(0, line_length, 2)

# ax.plot(x_vals_line, y_vals_line, z_vals_line, color='r', linewidth=2, label="Tangent line")

# ### LINE IN DIRECTION <1,1> STARTING AT (1, 2)
# t_vals = np.linspace(1, 5, 100)  # t ranges from 1 to 5
# x_vals = t_vals - 1  # Along the intersection, x = t - 1
# y_vals = t_vals  # Along the intersection, y = t
# z_vals = f(x_vals, y_vals)  # Corresponding z values from the surface

# ax.plot(x_vals, y_vals, z_vals, color='#000000', linewidth=2, label="Intersection line")

# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('f(x, y)')
# ax.set_title('Joint CDF f(x, y)')

plt.show()
