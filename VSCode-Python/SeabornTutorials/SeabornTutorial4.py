import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

tips = sns.load_dataset("tips")

sns.lmplot(data = tips, x = "total_bill", y = "tip", col = "time", hue = "smoker")
plt.show()
