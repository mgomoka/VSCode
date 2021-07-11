import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "ticks", palette = "pastel")

# Load The Example Tips Dataset
tips = sns.load_dataset("tips")

# Draw A Nested Boxplot To Show Bills By Day And Time
sns.boxplot(x = "day", y = "total_bill",
            hue = "smoker", palette = ["m", "g"],
            data = tips)
sns.despine(offset = 10, trim = True)

plt.show()
