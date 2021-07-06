# Importing MPlot3D Toolkits, Numpy and MatPlotLib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

# Syntax For 3-D Projection
ax = plt.axes(projection = '3d')

# Defining All 3 Axes
z = np.linspace(0, 1, 100)
x = z * np.sin(25 * z)
y = z * np.cos(25 * z)

# Plotting
ax.plot3D(x, y, z, 'green')
ax.set_title('3D Line Plot')
plt.show()
