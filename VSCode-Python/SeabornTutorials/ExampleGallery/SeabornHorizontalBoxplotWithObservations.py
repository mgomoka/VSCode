import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "ticks")

# Initialize The Figure With A Logarithmic x Axis
f, ax = plt.subplots(figsize = (7, 6))
ax.set_xscale("log")

# Load The Example Planets Dataset
planets = sns.load_dataset("planets")

# Plot The Orbital Period With Horizontal Boxes
sns.boxplot(x = "distance", y = "method", data = planets,
            whis = [0, 100], width = .6, palette = "vlag")

# Add In Points To Show Each Observation
sns.stripplot(x = "distance", y = "method", data = planets,
              size = 4, color = ".3", linewidth = 0)

# Tweak The Visual Presentation
ax.xaxis.grid(True)
ax.set(ylabel = "")
sns.despine(trim = True, left = True)

plt.show()
