import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid", palette = "muted")

# Load The Penguins Dataset
df = sns.load_dataset("penguins")

# Draw A Categorical Scatterplot To Show Each Observation
ax = sns.swarmplot(data = df, x = "body_mass_g", y = "sex", hue = "species")
ax.set(ylabel = "")

plt.show()
