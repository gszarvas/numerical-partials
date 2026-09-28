import sympy

x, y = sympy.symbols('x y')

# f = sympy.sympify(input("Enter a function in terms of x and y:\n"))
f = (1 - sympy.exp(-x)) * (1 - sympy.exp(-y))

x_0 = 1 # float(input("Enter a value of x:\n"))
y_0 = 1 # float(input("Enter a value of y:\n"))

dx = sympy.symbols('dx')
dy = sympy.symbols('dy')
g_x = ( f.subs({x: x_0 + dx, y: y_0}) - f.subs({x: x_0 - dx, y: y_0}) ) / (2*dx)
g_y = ( f.subs({x: x_0, y: y_0 + dy}) - f.subs({x: x_0, y: y_0 - dy}) ) / (2*dy)


tol = float(input("Enter tolerance:\n"))

h_x = 1
dec_factor = 0.5 # float(input("Enter h decrement factor:\n"))
estimate_0 = g_x.subs(dx, h_x)
print(f"1st estimate is {estimate_0.evalf()}")
h_x *= dec_factor
estimate_1 = g_x.subs(dx, h_x)
print(f"2nd estimate is {estimate_1.evalf()}")
iter_count = 0

while abs(estimate_1 - estimate_0) > tol:   # Absolute tolerance
# while abs(estimate_1 - estimate_0) > abs(estimate_1) * tol:   # Relative tolerance
    iter_count += 1
    estimate_0 = estimate_1
    h_x *= dec_factor     # h is constantly decremented by a factor
    estimate_1 = g_x.subs(dx, h_x)
    if not(h_x > 0):
        break

print(f"Loop exited on iter {iter_count} for tolerance {tol} and h decrement {dec_factor}\nFinal value of h: {h_x}")
print(f"Estimated x partial: {estimate_1.evalf()}")

h_y = 1
dec_factor = 0.5 # float(input("Enter h decrement factor:\n"))
estimate_0 = g_y.subs(dy, h_y)
print(f"1st estimate is {estimate_0.evalf()}")
h_y *= dec_factor
estimate_1 = g_y.subs(dy, h_y)
print(f"2nd estimate is {estimate_1.evalf()}")
iter_count = 0

while abs(estimate_0 - estimate_1) > tol:
    iter_count += 1
    # print(f"Current diff: {estimate_0 - estimate_1}") bug testing line
    estimate_0 = estimate_1
    h_y *= dec_factor     # h is constantly decremented by a factor
    estimate_1 = g_y.subs(dy, h_y)
    if not(h_y > 0):
        break

print(f"Loop exited on iter {iter_count} for tolerance {tol} and h decrement {dec_factor}\nFinal value of h: {h_y}")
print(f"Estimated y partial: {estimate_1.evalf()}")

