import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

tips = sns.load_dataset("tips")

sns.displot(data = tips, x = "total_bill", col = "time", kde = True)
plt.show()
