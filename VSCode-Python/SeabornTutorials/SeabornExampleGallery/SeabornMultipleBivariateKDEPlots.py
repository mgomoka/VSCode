import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "darkgrid")
iris = sns.load_dataset("iris")

# Set Up The Figure
f, ax = plt.subplots(figsize = (8, 8))
ax.set_aspect("equal")

# Draw A Contour Plot To Represent Each Bivariate Density
sns.kdeplot(
    data = iris.query("species != 'versicolor'"),
    x = "sepal_width",
    y = "sepal_length",
    hue = "species",
    thresh = .1,
)

plt.show()
