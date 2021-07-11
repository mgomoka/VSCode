import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")

# Load The Example Exercise Dataset
df = sns.load_dataset("exercise")

# Draw A Pointplot To Show Pulse As A Function Of Three Categorical Factors
g = sns.catplot(x = "time", y = "pulse", hue = "kind", col = "diet",
                capsize = .2, palette = "YlGnBu_d", height = 6, aspect = .75,
                kind = "point", data = df)
g.despine(left = True)

plt.show()
