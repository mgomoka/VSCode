import pygame as pg
from pymunk import space

fibonacci = []
x1, x2 = 0, 1
while x2 < 1000:
    fibonacci.append(x2)
    x1, x2 = x2, x1 + x2
print(fibonacci)

#print(pg.font.get_fonts())

pg.init()
pg.display.set_caption("Fibonacci")

size = (850, 850)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
font = pg.font.SysFont('avenir', 20)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    screen.fill((255, 255, 255))

    spacePrintCounter = 1
    for x in fibonacci:
        exString = str(x)
        text = font.render(exString, True, (0, 0, 0))
        screen.blit(text, [-20 + (spacePrintCounter*50), 400])
        spacePrintCounter += 1

    pg.display.update()
    clock.tick(60)
