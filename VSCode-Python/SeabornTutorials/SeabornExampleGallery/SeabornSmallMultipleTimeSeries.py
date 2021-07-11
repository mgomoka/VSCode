import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "dark")
flights = sns.load_dataset("flights")

# Plot Each Year's Time Series In Its Own Facet
g = sns.relplot(
    data = flights,
    x = "month", y = "passengers", col = "year", hue = "year",
    kind = "line", palette = "crest", linewidth = 4, zorder = 5,
    col_wrap = 3, height = 2, aspect = 1.5, legend = False,
)

# Iterate Over Each Subplot To Customize Further
for year, ax in g.axes_dict.items():

    # Add The Title As An Annotation Within The Plot
    ax.text(.8, .85, year, transform = ax.transAxes, fontweight = "bold")

    # Plot Every Year's Time Series In The Background
    sns.lineplot(
        data = flights, x = "month", y = "passengers", units = "year",
        estimator = None, color = ".7", linewidth = 1, ax = ax,
    )

# Reduce The Frequency Of The x Axis Ticks
ax.set_xticks(ax.get_xticks()[::2])

# Tweak The Supporting Aspects Of The Plot
g.set_titles("")
g.set_axis_labels("", "Passengers")
g.tight_layout()

plt.show()
