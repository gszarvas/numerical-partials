import math

def f(x):
    # return x**4 + x**3 - x**2 - x
    return 15*x**3 + 15*x**2 + 6*x + 1  # Bessel degree 3

def f_forward(x, h):
    return (f(x+h) - f(x)) / h

def f_backward(x, h):
    return (f(x) - f(x-h)) / h
    
def f_central(x, h):
    return (f(x+h) - f(x-h)) / (2*h)

x = 1
h = 1
dec_factor = 0.5
tol = float(input("Enter tolerance:\n"))

estimate_0 = f_backward(x, h)
h *= dec_factor
estimate_1 = f_backward(x, h)

iter_count = 0

while abs(estimate_1 - estimate_0) > tol:   # Absolute tolerance
# while abs(estimate_1 - estimate_0) > abs(estimate_1) * tol:   # Relative tolerance
    iter_count += 1
    estimate_0 = estimate_1
    h *= dec_factor
    estimate_1 = f_backward(x, h)
    if h <= 0:
        break

print(f"Loop exited on iteration {iter_count} with decrement factor {dec_factor} and tolerance {tol}\nFinal value of h: {h}")
print(f"Final estimate: {estimate_1}")
