import math

def x(t):
    return math.sin(2*t)
def y(t):
    return math.cos(3*t)

def f(x, y):
    return (x*y)**3 * y

def f_x(x, y, h):
    return (f(x + h, y) - f(x - h, y)) / (2 * h)
def f_y(x, y, h):
    return (f(x, y + h) - f(x, y - h)) / (2 * h)

def f_xxyy(x, y, h):
    return (1/(h**4)) * (f(x+h, y+h) - 2*f(x, y+h) + f(x-h,y+h) - 2*f(x+h,y) + 4*f(x,y) - 2*f(x-h,y) + f(x+h,y-h) - 2*f(x, y-h) + f(x-h,y-h))

def x_central(t, h):
    return (x(t + h) - x(t - h)) / (2 * h)
def y_central(t, h):
    return (y(t + h) - y(t - h)) / (2 * h)

def f_t(t, h):
    return f_x(x(t), y(t), h) * x_central(t, h) + f_y(x(t), y(t), h) * y_central(t, h)

tol = 0.00001

t = 3 * math.pi / 2
x_0 = 2
y_0 = 2
h = 1
dec_factor = 0.5 # float(input("Enter h decrement factor:\n"))
estimate_0 = f_xxyy(x_0, y_0, h)
print(f"1st estimate is {estimate_0}")
h *= dec_factor
estimate_1 = f_xxyy(x_0, y_0, h)
print(f"2nd estimate is {estimate_1}")
iter_count = 0

while abs(estimate_0 - estimate_1) > tol:
    iter_count += 1
    estimate_0 = estimate_1
    h *= dec_factor 
    estimate_1 = f_xxyy(x_0, y_0, h)
    if not(h > 0):
        break

print(f"Loop exited on iter {iter_count} for tolerance {tol} and h decrement {dec_factor}\nFinal value of h: {h}")
print(f"Estimated df/dt: {estimate_1}")

print(f"Exact: {72*x_0 * y_0**2}")