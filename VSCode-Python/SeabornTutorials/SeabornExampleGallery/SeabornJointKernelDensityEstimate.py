import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "ticks")

# Load The Penguins Dataset
penguins = sns.load_dataset("penguins")

# Show The Joint Distribution Using Kernel Density Estimation
g = sns.jointplot(
    data = penguins,
    x = "bill_length_mm", y = "bill_depth_mm", hue = "species",
    kind = "kde",
)

plt.show()
