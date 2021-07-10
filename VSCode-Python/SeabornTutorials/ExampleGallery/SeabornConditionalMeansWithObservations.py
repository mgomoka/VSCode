import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")
iris = sns.load_dataset("iris")

# "Melt" The Dataset To "Long-Form" Or "Tidy" Representation
iris = pd.melt(iris, "species", var_name = "measurement")

# Initialize The Figure
f, ax = plt.subplots()
sns.despine(bottom = True, left = True)

# Show Each Observation With A Scatterplot
sns.stripplot(x = "value", y = "measurement", hue = "species",
              data = iris, dodge = True, alpha = .25, zorder = 1)

# Show The Conditional Means
sns.pointplot(x = "value", y = "measurement", hue = "species",
              data = iris, dodge = .532, join = False, palette = "dark",
              markers = "d", scale = .75, ci = None)

# Improve The Legend 
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[3:], labels[3:], title =" species",
          handletextpad = 0, columnspacing = 1,
          loc = "lower right", ncol = 3, frameon = True)

plt.show()
