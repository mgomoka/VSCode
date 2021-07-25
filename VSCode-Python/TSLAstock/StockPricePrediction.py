import numpy as np
import pandas as pd

teslaDataSet = pd.read_csv("/Users/matthewgomoka/Desktop/TSLA.csv")

teslaDataSet = teslaDataSet[['Date', 'Close']]
newTesla = teslaDataSet.loc[884:1639]
newTesla = newTesla.drop('Date', axis = 1)
newTesla = newTesla.reset_index(Drop = True)
T = T.astype('float32')
T = np.eshape(T, (-1, 1))

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))
T = scaler.fit_transform(T)

