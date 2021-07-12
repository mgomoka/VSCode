import numpy as np
import time

startTimeArray = time.time()
myArray = np.array([(1, 1, 1), (2, 2, 2), (3, 3, 3)])
print(myArray)
myArray = np.append(myArray, [(4, 4, 4)], axis = 0)
print(myArray)
endTimeArray = time.time()
print(endTimeArray-startTimeArray)

startTimeList = time.time()
myList = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(myList)
myList.append([4, 4, 4])
print(myList)
endTimeList = time.time()
print(endTimeList-startTimeList)
