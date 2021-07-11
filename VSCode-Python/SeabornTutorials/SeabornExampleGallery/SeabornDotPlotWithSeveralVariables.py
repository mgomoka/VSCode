import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")

# Load The Dataset
crashes = sns.load_dataset("car_crashes")

# Make The PairGrid
g = sns.PairGrid(crashes.sort_values("total", ascending = False),
                 x_vars = crashes.columns[:-3], y_vars = ["abbrev"],
                 height = 10, aspect = .25)

# Draw A Dot Plot Using The Stripplot Function
g.map(sns.stripplot, size = 10, orient = "h", jitter = False,
      palette = "flare_r", linewidth = 1, edgecolor = "w")

# Use The Same x Axis Limits On All Columns And Add Better Labels
g.set(xlim=(0, 25), xlabel="Crashes", ylabel="")

# Use Semantically Meaningful Titles For The Columns
titles = ["Total crashes", "Speeding crashes", "Alcohol crashes",
          "Not distracted crashes", "No previous crashes"]

for ax, title in zip(g.axes.flat, titles):

    # Set A Different Title For Each Axes
    ax.set(title = title)

    # Make The Grid Horizontal Instead Of Vertical
    ax.xaxis.grid(False)
    ax.yaxis.grid(True)

sns.despine(left = True, bottom = True)

plt.show()
