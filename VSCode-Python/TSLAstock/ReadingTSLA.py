import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tslaDataSet = pd.read_csv("/Users/matthewgomoka/Desktop/TSLA.csv")

print("\n", "\n")
print(tslaDataSet.head(), "\n")
print(tslaDataSet, "\n")
print(tslaDataSet.tail(), "\n", "\n", "\n")
print(tslaDataSet.columns, "\n")
print(tslaDataSet.shape, "\n")
print(tslaDataSet.describe(), "\n", "\n", "\n")
print(tslaDataSet.isnull().sum(), "\n", "\n", "\n")

sns.set_theme()
sns.relplot(x='Date', y='Open', data = tslaDataSet)
plt.show()
