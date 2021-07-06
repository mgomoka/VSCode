from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Function For Z Axis
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 3))

# X And Y Axis
x = np.linspace(-1, 5, 10)
y = np.linspace(-1, 5, 10)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection = '3d')

# ax.contour3D Is Used To Plot A Contour Graph
ax.contour3D(X, Y, Z)
ax.set_title('3D Contour')
plt.show()
