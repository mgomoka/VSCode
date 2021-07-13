import numpy as np
import sys

listTemp = range(1000)
print("Size Of Each Element In LIST (bytes):", sys.getsizeof(listTemp))
print("Size Of The Whole LIST (bytes):", (sys.getsizeof(listTemp)*len(listTemp)))

arrayTemp = np.arange(1000)
print("Size Of Each Element In ARRAY (bytes):", arrayTemp.itemsize)
print("Size Of The Whole ARRAY (bytes):", (arrayTemp.itemsize*arrayTemp.size))
