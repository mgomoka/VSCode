import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([2, 3, 4])

def dotProduct(a, b):
    # total = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
    total = 0.0
    for i in range(max(len(a), len(b))):
        total += a[i]*b[i]

    return total

finalAnswer = dotProduct(array1, array2)

print(finalAnswer)
