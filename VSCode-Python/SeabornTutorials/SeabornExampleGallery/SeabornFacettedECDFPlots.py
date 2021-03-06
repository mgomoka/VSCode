import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "ticks")
mpg = sns.load_dataset("mpg")

colors = (250, 70, 50), (350, 70, 50)
cmap = sns.blend_palette(colors, input = "husl", as_cmap = True)
sns.displot(
    mpg,
    x = "displacement", col = "origin", hue = "model_year",
    kind = "ecdf", aspect = .75, linewidth = 2, palette = cmap,
)

plt.show()
