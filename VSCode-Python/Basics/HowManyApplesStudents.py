print("How many students?")
numStu = float(input())
print("How many apples?")
numApp = float(input())

eachNum = numApp // numStu
remainNum = numApp % numStu
print("Each student will receive " + str(int(eachNum)) + " apples with " + str(int(remainNum)) + " remaining.")
