import numpy as np
# JAQUEZ ANDRES NC 0074 fecha 22 octubre 2026
n0099 = np.array([10, 20, 30, 40, 50])
print(n0099)
print(n0099[0])
print(n0099[3])
print(n0099[-1])
print(n0099[-2])
print("-----------------------------------")

n0099 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(n0099)
print(n0099[0, 0])
print(n0099[1, 2])
print(n0099[-1, -1])
print(n0099[-2, -2])

print("-----------------------------------")
# 3D array 2x(2x3)

n0099 = np.array([
    # 0
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    # 1
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(n0099)
print(n0099[0, 0, 0])
print(n0099[1, 1, 2])
print("JAQUEZ ANDRES NC 0074 ")