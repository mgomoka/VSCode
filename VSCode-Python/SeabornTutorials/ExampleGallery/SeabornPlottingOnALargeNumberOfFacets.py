import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "ticks")

# Create A Dataset With Many Short Random Walks
rs = np.random.RandomState(4)
pos = rs.randint(-1, 2, (20, 5)).cumsum(axis = 1)
pos -= pos[:, 0, np.newaxis]
step = np.tile(range(5), 20)
walk = np.repeat(range(20), 5)
df = pd.DataFrame(np.c_[pos.flat, step, walk],
                  columns = ["position", "step", "walk"])

# Initialize A Grid Of Plots With An Axes For Each Walk
grid = sns.FacetGrid(df, col = "walk", hue = "walk", palette = "tab20c",
                     col_wrap = 4, height = 1.5)

# Draw A Horizontal Line To Show The Starting Point
grid.map(plt.axhline, y = 0, ls = ":", c = ".5")

# Draw A Line Plot To Show The Trajectory Of Each Random Walk
grid.map(plt.plot, "step", "position", marker = "o")

# Adjust The Tick Positions And Labels
grid.set(xticks = np.arange(5), yticks = [-3, 3],
         xlim = (-.5, 4.5), ylim = (-3.5, 3.5))

# Adjust The Arrangement Of The Plots
grid.fig.tight_layout(w_pad = 1)

plt.show()
