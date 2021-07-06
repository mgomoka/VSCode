# https://matplotlib.org/3.1.0/gallery/mplot3d/trisurf3d_2.html

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as mtri

# This Import Registers The 3D Projection, But Is Otherwise Unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 Unused Import

fig = plt.figure(figsize = plt.figaspect(0.5))

# ============
#  FIRST PLOT
# ============

# Make A Mesh In The Space Of Parameterisation Variables u And v.
u = np.linspace(0, 2.0 * np.pi, endpoint = True, num = 50)
v = np.linspace(-0.5, 0.5, endpoint = True, num = 10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()

# This Is The Mobius Mapping, Taking A u, v Pair And Returning An x, y, z Triple.
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)

# Triangulate Parameter Space To Determine The Triangles.
tri = mtri.Triangulation(u, v)

# Plot The Surface. The Triangles In Parameter Space Determine Which x, y, z Points Are Connected By An Edge.
ax = fig.add_subplot(1, 2, 1, projection = '3d')
ax.plot_trisurf(x, y, z, triangles = tri.triangles, cmap = plt.cm.Spectral)
ax.set_zlim(-1, 1)

# ============
#  SECOND PLOT
# ============

# Make Parameter Spaces Radii And Angles.
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2*np.pi, n_angles, endpoint = False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis = 1)
angles[:, 1::2] += np.pi/n_angles

# Map Radius, Angle Pairs To x, y, z Points.
x = (radii*np.cos(angles)).flatten()
y = (radii*np.sin(angles)).flatten()
z = (np.cos(radii)*np.cos(3*angles)).flatten()

# Create The Triangulation; No Triangles So Delaunay Triangulation Created.
triang = mtri.Triangulation(x, y)

# Mask Off Unwanted Triangles.
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)

# Plot The Surface.
ax.set_title('More Triangular Surfaces')
ax = fig.add_subplot(1, 2, 2, projection = '3d')
ax.plot_trisurf(triang, z, cmap = plt.cm.CMRmap)
plt.show()
