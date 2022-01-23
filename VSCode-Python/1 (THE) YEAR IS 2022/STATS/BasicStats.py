import math
import numpy as np

# sampleArray = [2, 3, 4]
# print(np.mean(sampleArray))
# print(np.std(sampleArray))

def findRvalue(xArray, yArray):
    rValue = 0
    for x in range(len(xArray)):
        rValue += ((((xArray[x])-(np.mean(xArray))) / (np.std(xArray))) * (((yArray[x])-(np.mean(yArray))) / (np.std(yArray))))
    rValue /= ((int(len(xArray)))-1)
    print(int(len(xArray)))
    return rValue

continueApplication = True
while continueApplication == True:
    print("1 Find Mean & Standard Deviation Of Single Set\n2 Find Means & Standard Deviations Of Pair\n3 Find Least Squares Regression Line\n4 Close Application\n")
    mainMenuInput = int(input("Input: "))
    if mainMenuInput == 1:
        tempNumberOfInputs = int(input("How Many Values?: "))
        tempInputArray = []
        tempCounter = 0
        print("\nEnter Each Value Followed By Enter.")
        while tempCounter < tempNumberOfInputs:
            tempInputArray.append(int(input()))
            tempCounter += 1
        print("\n" + "Sample Mean = " + str(np.mean(tempInputArray)))
        print("Sample Standard Deviation = " + str(np.std(tempInputArray)) + "\n")
    elif mainMenuInput == 2:
        tempNumberOfInputs = int(input("How Many Value Pairs?: "))
        tempInputArrayX = []
        tempInputArrayY = []
        tempCounter = 0
        print("\nEnter Each X Value Followed By Enter.")
        while tempCounter < tempNumberOfInputs:
            tempInputArrayX.append(int(input()))
            tempCounter += 1
        tempCounter = 0
        print("\nEnter Each Y Value Followed By Enter.")
        while tempCounter < tempNumberOfInputs:
            tempInputArrayY.append(int(input()))
            tempCounter += 1
        print("\n" + "Sample Mean X = " + str(np.mean(tempInputArrayX)))
        print("Sample Standard Deviation X = " + str(np.std(tempInputArrayX))) 
        print("Sample Mean Y = " + str(np.mean(tempInputArrayY)))
        print("Sample Standard Deviation Y = " + str(np.std(tempInputArrayY)) + "\n")
    elif mainMenuInput == 3:
        tempNumberOfInputs = int(input("How Many Value Pairs?: "))
        tempInputArrayX = []
        tempInputArrayY = []
        tempCounter = 0
        print("\nEnter Each X Value Followed By Enter.")
        while tempCounter < tempNumberOfInputs:
            tempInputArrayX.append(int(input()))
            tempCounter += 1
        tempCounter = 0
        print("\nEnter Each Y Value Followed By Enter.")
        while tempCounter < tempNumberOfInputs:
            tempInputArrayY.append(int(input()))
            tempCounter += 1
        print("\n" + "Sample Mean X = " + str(np.mean(tempInputArrayX)))
        print("Sample Standard Deviation X = " + str(np.std(tempInputArrayX))) 
        print("Sample Mean Y = " + str(np.mean(tempInputArrayY)))
        print("Sample Standard Deviation Y = " + str(np.std(tempInputArrayY)))
        print("R Coefficient = " + str(findRvalue(tempInputArrayX, tempInputArrayY)) + "\n")
    elif mainMenuInput == 4:
        continueApplication = False
