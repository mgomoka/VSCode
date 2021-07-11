import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")

# Initialize The MatPlotLib Figure
f, ax = plt.subplots(figsize = (6, 15))

# Load The Example Car Crash Dataset
crashes = sns.load_dataset("car_crashes").sort_values("total", ascending = False)

# Plot The Total Crashes
sns.set_color_codes("pastel")
sns.barplot(x = "total", y = "abbrev", data = crashes,
            label = "Total", color = "b")

# Plot The Crashes Where Alcohol Was Involved
sns.set_color_codes("muted")
sns.barplot(x = "alcohol", y = "abbrev", data = crashes,
            label = "Alcohol-involved", color = "b")

# Add A Legend And Informative Axis Label
ax.legend(ncol = 2, loc = "lower right", frameon = True)
ax.set(xlim = (0, 24), ylabel = "",
       xlabel = "Automobile collisions per billion miles")
sns.despine(left = True, bottom = True)

plt.show()
