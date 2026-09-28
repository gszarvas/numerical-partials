## second order partials ##

import sympy

x, y = sympy.symbols('x y')

# f = sympy.sympify(input("Enter a function in terms of x and y:\n"))
f = (1 - sympy.exp(-x)) * (1 - sympy.exp(-y))
# f = sympy.exp(-(x**2 + y**2))


x_0 = 0 # float(input("Enter a value of x:\n"))
y_0 = 0 # float(input("Enter a value of y:\n"))

dx = sympy.symbols('dx')
dy = sympy.symbols('dy')

# f_x approximation
# g = ( f.subs({x: x_0 + dx, y: y_0}) - f.subs({x: x_0 - dx, y: y_0}) ) / (2*dx)

# f_y approximation
# g_y = ( f.subs({x: x_0, y: y_0 + dy}) - f.subs({x: x_0, y: y_0 - dy}) ) / (2*dy)

# f_xy approximation
g = ( f.subs({x: x_0 + dx, y: y_0 + dy}) - f.subs({x: x_0 + dx, y: y_0 - dy}) - f.subs({x: x_0 - dx, y: y_0 + dy}) + f.subs({x: x_0 - dx, y: y_0 - dy}) ) / (4 * dx * dy)

# f_xx approximation
# g = ( f.subs({x: x_0 + 2*dx, y: y_0}) - 2*f.subs({x: x_0, y: y_0}) + f.subs({x: x_0 - 2*dx, y: y_0}) ) / (4 * dx * dy)

# f_yy approximation
# g = ( f.subs({x: x_0, y: y_0 + 2*dy}) - 2*f.subs({x: x_0, y: y_0}) + f.subs({x: x_0, y: y_0 - 2*dy}) ) / (4 * dx * dy)

h = 1
dec_factor = 0.5 # float(input("Enter h decrement factor:\n"))
estimate_0 = g.subs({dx: h, dy: h})
print(f"1st estimate is {estimate_0.evalf()}")
h *= dec_factor
estimate_1 = g.subs({dx: h, dy: h})
print(f"2nd estimate is {estimate_1.evalf()}")
iter_count = 0

tol = 0.00001 # float(input("Enter tolerance:\n"))

# while abs(estimate_1 - estimate_0) > tol:   # Absolute tolerance
while abs(estimate_0 - estimate_1) > abs(estimate_1) * tol: # Relative
    iter_count += 1
    estimate_0 = estimate_1
    h *= dec_factor     # h is constantly decremented by a factor 
    estimate_1 = g.subs({dx: h, dy: h})
    if not(h > 0):
        break

print(f"Loop exited on iter {iter_count} for tolerance {tol} and h decrement {dec_factor}\nFinal value of h: {h}")
print(f"Estimated yy partial: {estimate_1.evalf()}")  # change output description as needed
