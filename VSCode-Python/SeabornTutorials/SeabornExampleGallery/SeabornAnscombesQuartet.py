import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "ticks")

# Load The Example Dataset For Anscombe's Quartet
df = sns.load_dataset("anscombe")

# Show The Results Of A Linear Regression Within Each Dataset
sns.lmplot(x = "x", y = "y", col = "dataset", hue = "dataset", data = df,
           col_wrap = 2, ci = None, palette = "muted", height = 4,
           scatter_kws = {"s": 50, "alpha": 1})

plt.show()
