import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")

# Make An Example Dataset With y ~ x
rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)

# Plot The Residuals After Fitting A Linear Model
sns.residplot(x = x, y = y, lowess = True, color = "g")

plt.show()

'''
NOT WORKING
'''
