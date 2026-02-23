import numpy as np

def on_line_2x(p):      # пряма y = 2x
    return np.isclose(p[1], 2*p[0])

def on_line_2x_plus_1(p):  # пряма y = 2x + 1
    return np.isclose(p[1], 2*p[0] + 1)

direction = np.array([1.0, 2.0])

# підпростір: y = 2x
v1 = 3 * direction
v2 = -1.5 * direction
alpha = 2.7

sum_ok_sub = on_line_2x(v1 + v2)
scale_ok_sub = on_line_2x(alpha * v1)

# не підпростір: y = 2x + 1
p1 = np.array([0.0, 1.0])
p2 = np.array([1.0, 3.0])

sum_ok_shift = on_line_2x_plus_1(p1 + p2)
scale_ok_shift = on_line_2x_plus_1(alpha * p1)

print("y = 2x  сума ->", sum_ok_sub, "  множення ->", scale_ok_sub)
print("y = 2x+1 сума ->", sum_ok_shift, "  множення ->", scale_ok_shift)


# y = 2x  сума -> True   множення -> True
# y = 2x+1 сума -> False   множення -> False
