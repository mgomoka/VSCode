'''
http://seaborn.pydata.org/introduction.html
'''

# Import Seaborn && MatPlotLib
import seaborn as sns
import matplotlib.pyplot as plt

# Apply The Default Theme
sns.set_theme()

# Load An Example Dataset
tips = sns.load_dataset("tips")

# Create Visualization
sns.relplot(data = tips, x = "total_bill", y = "tip", col = "time", hue = "smoker", style = "smoker", size = "size")
plt.show()
