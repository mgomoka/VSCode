print()
print("Input Timestaps Format:")
print("HHMMSS")
print()
print("1 Second = 000001")
print("60 Seconds = 000060")
print("1 Minute = 000100")
print("60 Minutes = 006000")
print("1 Hour = 010000")
print("99 Hours = 990000")
print()
print("First Timestap:")
first = input()
print("Second Timestap:")
second = input()

firstArray = []
secondArray = []

for xFirst in range(3):
    firstArray.append(first[xFirst*2] + first[xFirst*2+1])
for xSecond in range(3):
    secondArray.append(second[xSecond*2] + second[xSecond*2+1])

firstTotalSecond = int(firstArray[2]) + (int(firstArray[1]) * 60) + (int(firstArray[0]) * 60 * 60)
secondTotalSecond = int(secondArray[2]) + (int(secondArray[1]) * 60) + (int(secondArray[0]) * 60 * 60)
differenceInSeconds = abs(firstTotalSecond - secondTotalSecond)
print("The difference is " + str(differenceInSeconds) + " seconds.")
