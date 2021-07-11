import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

# Load The Penguins Dataset
penguins = sns.load_dataset("penguins")

# Plot Sepal Width As A Function Of sepal_length Across Days
g = sns.lmplot(
    data = penguins,
    x = "bill_length_mm", y = "bill_depth_mm", hue = "species",
    height = 5
)

# Use More Informative Axis Labels Than Are Provided By Default
g.set_axis_labels("Snoot length (mm)", "Snoot depth (mm)")

plt.show()
