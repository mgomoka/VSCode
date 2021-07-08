import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

penguins = sns.load_dataset("penguins")

sns.jointplot(data = penguins, x = "flipper_length_mm", y = "bill_length_mm", hue = "species")
plt.show()
