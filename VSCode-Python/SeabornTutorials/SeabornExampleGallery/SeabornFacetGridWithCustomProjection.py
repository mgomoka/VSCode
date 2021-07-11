import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

# Generate An Example Radial Datast
r = np.linspace(0, 10, num = 100)
df = pd.DataFrame({'r': r, 'slow': r, 'medium': 2 * r, 'fast': 4 * r})

# Convert The Dataframe To Long-Form Or "Tidy" Format
df = pd.melt(df, id_vars = ['r'], var_name = 'speed', value_name = 'theta')

# Set Up A Grid Of Axes With A Polar Projection
g = sns.FacetGrid(df, col = "speed", hue = "speed",
                  subplot_kws = dict(projection = 'polar'), height = 4.5,
                  sharex = False, sharey = False, despine = False)

# Draw A Scatterplot Onto Each Axes In The Grid
g.map(sns.scatterplot, "theta", "r")

plt.show()
