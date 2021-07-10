import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "darkgrid")

# Load The Example Titanic Dataset
df = sns.load_dataset("titanic")

# Make A Custom Palette With Gendered Colors
pal = dict(male = "#6495ED", female = "#F08080")

# Show The Survival Probability As A Function Of Age And Sex
g = sns.lmplot(x = "age", y = "survived", col = "sex", hue = "sex", data = df,
               palette = pal, y_jitter = .02, logistic = True, truncate = False)
g.set(xlim = (0, 80), ylim = (-.05, 1.05))

plt.show()

'''
NOT WORKING
'''
