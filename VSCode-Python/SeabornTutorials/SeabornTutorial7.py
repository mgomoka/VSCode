import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

tips = sns.load_dataset("tips")

sns.catplot(data = tips, kind = "swarm", x = "day", y = "total_bill", hue = "smoker")
plt.show()
