import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "white", rc = {"axes.facecolor": (0, 0, 0, 0)})

# Create The Data
rs = np.random.RandomState(1979)
x = rs.randn(500)
g = np.tile(list("ABCDEFGHIJ"), 50)
df = pd.DataFrame(dict(x = x, g = g))
m = df.g.map(ord)
df["x"] += m

# Initialize The FacetGrid Object
pal = sns.cubehelix_palette(10, rot = -.25, light = .7)
g = sns.FacetGrid(df, row = "g", hue = "g", aspect = 15, height = .5, palette = pal)

# Draw The Densities In A Few Steps
g.map(sns.kdeplot, "x",
      bw_adjust = .5, clip_on = False,
      fill = True, alpha = 1, linewidth = 1.5)
g.map(sns.kdeplot, "x", clip_on = False, color = "w", lw = 2, bw_adjust = .5)
g.map(plt.axhline, y = 0, lw = 2, clip_on = False)

# Define And Use A Simple Function To Label The Plot In Axes Coordinates
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight = "bold", color = color,
            ha = "left", va = "center", transform = ax.transAxes)

g.map(label, "x")

# Set The Subplots To Overlap
g.fig.subplots_adjust(hspace = -.25)

# Remove Axes Details That Don't Play Well With Overlap
g.set_titles("")
g.set(yticks = [])
g.despine(bottom = True, left = True)

plt.show()
