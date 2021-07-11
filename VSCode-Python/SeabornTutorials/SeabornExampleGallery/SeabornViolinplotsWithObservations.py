import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

# Create A Random Dataset Across Several Variables
rs = np.random.default_rng(0)
n, p = 40, 8
d = rs.normal(0, 2, (n, p))
d += np.log(np.arange(1, p + 1)) * -5 + 10

# Show Each Distribution With Both Violins And Points
sns.violinplot(data = d, palette = "light:g", inner = "points", orient = "h")

plt.show()
