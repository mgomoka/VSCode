'''
R = 1.097e-2
for m in range(1, 4):
    print("Series for m =", m)
    for n in range(m+1, m+6):
        invlambda = R * ((1/m**2) - (1/n**2))
        print("  ", 1/invlambda, "nm")
'''



howmanyMdoyouwant = 50

R = 1.097e-2
m = [[] for _ in range(howmanyMdoyouwant)]

for loopCounter1 in range(1, howmanyMdoyouwant+1):
    m[loopCounter1-1].append(loopCounter1)
    for loopCounter2 in range(loopCounter1+1, loopCounter1+6):
        invlambda = R * ((1/loopCounter1**2) - (1/loopCounter2**2))
        vlamdba = 1/invlambda
        m[loopCounter1-1].append(vlamdba)


for x in range(3):
    print()
print("The emission spectrum of atomic hydrogen has been divided into a number of spectral series, with wavelengths given by the Rydberg formula.")
print("These observed spectral lines are due to the electron making transitions between two energy levels in an atom.")
print("The classification of the series by the Rydberg formula was important in the development of quantum mechanics.")
print("The spectral series are important in astronomical spectroscopy for detecting the presence of hydrogen and calculating red shifts.")
print()
varList = []
for x in range(1, howmanyMdoyouwant+1):
    for y in range(0, 5):
        varList.append(m[x-1][y+1])
    if x < 7:
        print("M", m[x-1][0], " = ", varList)
        print()
    else:
        print("M", m[x-1][0], " = ", varList) 
    varList.clear()
'''
print("M", m[0][0], " = ", m[0][1], m[0][2], m[0][3], m[0][4], m[0][5])
print("M", m[1][0], " = ", m[1][1], m[1][2], m[1][3], m[1][4], m[1][5])
print("M", m[2][0], " = ", m[2][1], m[2][2], m[2][3], m[2][4], m[2][5])
'''




import pygame as pg
import sys

pg.init()
pg.display.set_caption("Rydberg")

size = (850, 850)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
font = pg.font.SysFont('avenir', 12)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    oneString = 'The emission spectrum of atomic hydrogen has been divided into a number of spectral series, with wavelengths given by the Rydberg formula.'
    text = font.render(oneString, True, (0, 0, 0))
    screen.blit(text, [20, 20])
    twoString = 'These observed spectral lines are due to the electron making transitions between two energy levels in an atom.'
    text = font.render(twoString, True, (0, 0, 0))
    screen.blit(text, [20, 32])
    threeString = 'The classification of the series by the Rydberg formula was important in the development of quantum mechanics.'
    text = font.render(threeString, True, (0, 0, 0))
    screen.blit(text, [20, 44])
    fourString = 'The spectral series are important in astronomical spectroscopy for detecting the presence of hydrogen and calculating red shifts.'
    text = font.render(fourString, True, (0, 0, 0))
    screen.blit(text, [20, 56])

    varListTwoPointO = []
    for x in range(1, howmanyMdoyouwant+1):
        for y in range(0, 5):
            varListTwoPointO.append(m[x-1][y+1])
        if x <= 50:
            textTemp = 'M' + str(m[x-1][0]) + " = " + str(varListTwoPointO)
            textTwo = font.render(textTemp, True, (0, 0, 0))
            screen.blit(textTwo, [20, 200+(12*x)])
        varListTwoPointO.clear()

    pg.display.update()
    clock.tick(60)
