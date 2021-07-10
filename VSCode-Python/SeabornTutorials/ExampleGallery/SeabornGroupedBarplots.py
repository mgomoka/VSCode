import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")

penguins = sns.load_dataset("penguins")

# Draw A Nested Barplot By Species And Sex
g = sns.catplot(
    data = penguins, kind = "bar",
    x = "species", y = "body_mass_g", hue = "sex",
    ci = "sd", palette = "dark", alpha = .6, height = 6
)
g.despine(left = True)
g.set_axis_labels("", "Body mass (g)")
g.legend.set_title("")

plt.show()
