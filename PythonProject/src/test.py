import numpy as np
# x = (2,3)
# x[0] = 5
# print(x)


y = np.arange(0,9).reshape(3,3)
print(y)

z = (y > 5) & (y < 8) # mask
# # need to get indexes where z evaluates to true
print(z)
print(y[z])
y[z] = 0 # threshold
print(y)
# print(y)
# y[y > 5] = 0
# print(y)


def something():
    return [5,4]

x, y = something()
print(x)
print(y)