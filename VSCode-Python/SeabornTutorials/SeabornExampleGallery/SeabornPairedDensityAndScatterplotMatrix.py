import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "white")

df = sns.load_dataset("penguins")

g = sns.PairGrid(df, diag_sharey = False)
g.map_upper(sns.scatterplot, s = 15)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot, lw = 2)

plt.show()
