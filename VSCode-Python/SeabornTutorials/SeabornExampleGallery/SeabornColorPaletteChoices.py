import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "white", context = "talk")
rs = np.random.RandomState(8)

# Set Up The MatPlotLib Figure
f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize = (7, 5), sharex = True)

# Generate Some Sequential Data
x = np.array(list("ABCDEFGHIJ"))
y1 = np.arange(1, 11)
sns.barplot(x = x, y = y1, palette = "rocket", ax = ax1)
ax1.axhline(0, color = "k", clip_on = False)
ax1.set_ylabel("Sequential")

# Center The Data To Make It Diverging
y2 = y1 - 5.5
sns.barplot(x = x, y = y2, palette = "vlag", ax = ax2)
ax2.axhline(0, color = "k", clip_on = False)
ax2.set_ylabel("Diverging")

# Randomly Reorder The Data To Make It Qualitative
y3 = rs.choice(y1, len(y1), replace = False)
sns.barplot(x = x, y = y3, palette = "deep", ax = ax3)
ax3.axhline(0, color = "k", clip_on = False)
ax3.set_ylabel("Qualitative")

# Finalize The Plot
sns.despine(bottom = True)
plt.setp(f.axes, yticks = [])
plt.tight_layout(h_pad = 2)

plt.show()
