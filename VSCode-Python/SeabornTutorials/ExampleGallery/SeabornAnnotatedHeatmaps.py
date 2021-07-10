import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

# Load The Example Flights Dataset And Convert To Long-Form
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

# Draw A Heatmap With The Numeric Values In Each Cell
f, ax = plt.subplots(figsize = (9, 6))
sns.heatmap(flights, annot = True, fmt = "d", linewidths = .5, ax = ax)
plt.show()
