import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "ticks")

dots = sns.load_dataset("dots")

# Define The Palette As A List To Specify Exact Values
palette = sns.color_palette("rocket_r")

# Plot The Lines On Two Facets
sns.relplot(
    data = dots,
    x = "time", y = "firing_rate",
    hue = "coherence", size = "choice", col = "align",
    kind = "line", size_order = ["T1", "T2"], palette = palette,
    height = 5, aspect = .75, facet_kws = dict(sharex = False),
)

plt.show()
