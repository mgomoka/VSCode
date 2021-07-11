import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "dark")

diamonds = sns.load_dataset("diamonds")
sns.displot(
    data = diamonds, x = "price", y = "color", col = "clarity",
    log_scale = (True, False), col_wrap = 4, height = 4, aspect = .7,
)

plt.show()
