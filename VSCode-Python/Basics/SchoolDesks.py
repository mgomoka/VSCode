print()
print("How many students in classroom 1?")
oneStudents = int(input())
print("How many students in classroom 2?")
twoStudents = int(input())
print("How many students in classroom 3?")
threeStudents = int(input())

roomOneDesk = 0
roomTwoDesk = 0
roomThreeDesk = 0
remainOne = oneStudents % 2
remainTwo = twoStudents % 2
remainThree = threeStudents % 2

if remainOne == 0:
    roomOneDesk = oneStudents // 2
if remainOne == 1:
    roomOneDesk = (oneStudents // 2) + 1
if remainTwo == 0:
    roomTwoDesk = twoStudents // 2
if remainTwo == 1:
    roomTwoDesk = (twoStudents // 2) + 1
if remainThree == 0:
    roomThreeDesk = threeStudents // 2
if remainThree == 1:
    roomThreeDesk = (threeStudents // 2) + 1

print()
print("Classroom 1 will need " + str(roomOneDesk) + " desks.")
print("Classroom 2 will need " + str(roomTwoDesk) + " desks.")
print("Classroom 3 will need " + str(roomThreeDesk) + " desks.")
print()
