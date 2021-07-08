print("Would you like to find the area of a right angled triangle?")
init = str(input())
'''
if init == 'yes':
    init = 'y'
'''

inputLength = len(init)
for x in range(inputLength):
    if init[x] == 'y':
        init = 'y'
        break

while init == 'y':

    print("Height:")
    height = float(input())
    print("Width:")
    width = float(input())
    area = (height * width) / 2
    print("Area:", area)
    print("Would you like to find the area of another right angled triangle?")
    init = str(input())
    inputLength = len(init)
    for x in range(inputLength):
        if init[x] == 'y':
            init = 'y'
            break
