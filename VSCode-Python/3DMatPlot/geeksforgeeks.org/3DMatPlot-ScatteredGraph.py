# Importing MPlot3D Toolkits
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

# Syntax For 3-D Projection
ax = plt.axes(projection = '3d')

# Defining Axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)
c = x + y
ax.scatter(x, y, z, c = c)

# Syntax For Plotting
ax.set_title('3d Scatter Plot')
plt.show()
