from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "white")

# Generate A Large Random Dataset
rs = np.random.RandomState(33)
d = pd.DataFrame(data = rs.normal(size = (100, 26)),
                 columns = list(ascii_letters[26:]))

# Compute The Correlation Matrix
corr = d.corr()

# Generate A Mask For The Upper Triangle
mask = np.triu(np.ones_like(corr, dtype = bool))

# Set Up The MatPlotLib Figure
f, ax = plt.subplots(figsize = (11, 9))

# Generate A Custom Diverging Colormap
cmap = sns.diverging_palette(230, 20, as_cmap = True)

# Draw The Heatmap With The Mask And Correct Aspect Ratio
sns.heatmap(corr, mask = mask, cmap = cmap, vmax = .3, center = 0,
            square = True, linewidths = .5, cbar_kws = {"shrink": .5})

plt.show()
