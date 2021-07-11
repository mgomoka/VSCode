import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")

# Load The Example Titanic Dataset
titanic = sns.load_dataset("titanic")

# Set Up A Grid To Plot Survival Probability Against Several Variables
g = sns.PairGrid(titanic, y_vars = "survived",
                 x_vars = ["class", "sex", "who", "alone"],
                 height = 5, aspect = .5)

# Draw A Seaborn Pointplot Onto Each Axes
g.map(sns.pointplot, scale = 1.3, errwidth = 4, color = "xkcd:plum")
g.set(ylim = (0, 1))
sns.despine(fig = g.fig, left = True)

plt.show()
