import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")

# Load The Example Tips Dataset
tips = sns.load_dataset("tips")

# Draw A Nested Violinplot And Split The Violins For Easier Comparison
sns.violinplot(data = tips, x = "day", y = "total_bill", hue = "smoker",
               split = True, inner = "quart", linewidth = 1,
               palette = {"Yes": "b", "No": ".85"})
sns.despine(left = True)

plt.show()
