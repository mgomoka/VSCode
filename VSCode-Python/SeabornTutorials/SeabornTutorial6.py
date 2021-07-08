import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

tips = sns.load_dataset("tips")

sns.displot(data = tips, kind = "ecdf", x = "total_bill", col = "time", hue = "smoker", rug = True)
plt.show()
