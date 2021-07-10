import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "ticks")

# Load The Planets Dataset And Initialize The Figure
planets = sns.load_dataset("planets")
g = sns.JointGrid(data = planets, x = "year", y = "distance", marginal_ticks = True)

# Set A Log Scaling On The y Axis
g.ax_joint.set(yscale = "log")

# Create An Inset Legend For The Histogram Colorbar
cax = g.fig.add_axes([.15, .55, .02, .2])

# Add The Joint And Marginal Histogram Plots
g.plot_joint(
    sns.histplot, discrete = (True, False),
    cmap = "light:#03012d", pmax = .8, cbar = True, cbar_ax = cax
)
g.plot_marginals(sns.histplot, element = "step", color = "#03012d")

plt.show()
