userInputs = []
print("Would you like to enter a number?")
yayNay = str(input())

ynLength = len(yayNay)
for x in range(ynLength):
    if yayNay[x] == 'y':
        yayNay = 'y'
        break

while yayNay == 'y':
    print()
    print("Please enter the number:")
    userInputs.append(int(input()))

    print()
    print("Would you like to add another number to the list?")
    yayNay = str(input())
    ynLength = len(yayNay)
    for x in range(ynLength):
        if yayNay[x] == 'y':
            yayNay = 'y'
            break

userInputs.sort()
# userInputs.reverse()

print()
print(userInputs)
