"""

Code From Article 'Can Integer Operations Overflow in Python?'
Article: https://mortada.net/can-integer-operations-overflow-in-python.html

"""

import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize
figsize(15, 5)

import numpy as np
import pandas as pd

import sys
int_sizes = {}
for i in range(160):
    int_sizes[i] = sys.getsizeof(2 ** i)
int_sizes = pd.Series(int_sizes)

ax = int_sizes.plot(ylim = [0, 60])
ax.set_ylabel('Number Of Bytes')
ax.set_xlabel('Integer (Log Scale)')
ax.set_title('Number Of Bytes Used To Store An Integer (Python 3.4)')
ax.set_xticks(range(0, 160, 10))
labels = ['$2^{%d}$' % x for x in range(0, 160, 10)]
ax.set_xticklabels(labels)
ax.tick_params(axis = 'x', labelsize = 18)
ax.tick_params(axis = 'y', labelsize = 12)

print(int_sizes[29:31].head())

plt.show()
