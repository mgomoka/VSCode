import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")

# Load The Diamonds Dataset
diamonds = sns.load_dataset("diamonds")

# Plot The Distribution Of Clarity Ratings, Conditional On Carat
sns.displot(
    data = diamonds,
    x = "carat", hue = "cut",
    kind = "kde", height = 6,
    multiple = "fill", clip = (0, None),
    palette = "ch:rot=-.25,hue=1,light=.75",
)

plt.show()
