import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

penguins = sns.load_dataset("penguins")

sns.relplot(
    data = penguins,
    x = "bill_length_mm", y = "bill_depth_mm",
    hue = "body_mass_g",
)
plt.show()
