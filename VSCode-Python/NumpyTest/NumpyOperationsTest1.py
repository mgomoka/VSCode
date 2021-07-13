import numpy as np

myList = [1, 2, 3]
myArray = np.array(myList)

try:
    myList = myList + 9
    print("Lists Support LIST+INT")
except:
    print("Lists Don't Support LIST+INT")

try:
    myArray = myArray + 9
    print("Numpy Arrays Support LIST+INT") 
    print("Modified Numpy Array:", myArray)
except:
    print("Numpy Arrays Don't Support LIST+INT")
