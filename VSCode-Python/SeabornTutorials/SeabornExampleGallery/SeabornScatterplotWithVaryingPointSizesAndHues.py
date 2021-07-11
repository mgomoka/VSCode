import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "white")

# Load The Example mpg Dataset
mpg = sns.load_dataset("mpg")

# Plot Miles Per Gallon Against Horsepower With Other Semantics
sns.relplot(x = "horsepower", y = "mpg", hue = "origin", size = "weight",
            sizes = (40, 400), alpha = .5, palette = "muted",
            height = 6, data = mpg)

plt.show()
