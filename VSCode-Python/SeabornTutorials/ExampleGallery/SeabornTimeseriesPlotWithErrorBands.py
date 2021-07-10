import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "darkgrid")

# Load An Example Dataset With Long-Form Data
fmri = sns.load_dataset("fmri")

# Plot The Responses For Different Events And Regions
sns.lineplot(x = "timepoint", y = "signal",
             hue = "region", style = "event",
             data = fmri)

plt.show()
