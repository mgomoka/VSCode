# https://matplotlib.org/stable/gallery/mplot3d/trisurf3d.html

import matplotlib.pyplot as plt
import numpy as np

n_radii = 8
n_angles = 36

# Make Radii And Angles Spaces (Radius r=0 Omitted To Eliminate Duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]

# Convert Polar (radii, angles) Coords To Cartesian (x, y) Coords.
# (0, 0) Is Manually Added At This Stage, So There Will Be No Duplicate Points In The (x, y) Plane.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Compute z To Make The Pringle Rurface.
z = np.sin(-x*y)

ax = plt.figure().add_subplot(projection='3d')

ax.plot_trisurf(x, y, z, linewidth = 0.2, antialiased = True)
ax.set_title('Triangular Surfaces')
plt.show()
