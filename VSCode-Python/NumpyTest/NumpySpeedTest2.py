import numpy as np
import time

size = 1000000

listOne = range(size)
listTwo = range(size)
arrayOne = np.arange(size)
arrayTwo = np.arange(size)

initListTime = time.time()
resultList = [(a * b) for a, b in zip(listOne, listTwo)]
endListTime = time.time()
print("Time Taken By LISTS:", (endListTime-initListTime), "seconds.")

initArrayTime = time.time()
resultArray = arrayOne * arrayTwo
endArrayTime = time.time()
print("Time Taken By ARRAYS:", (endArrayTime-initArrayTime), "seconds.")
