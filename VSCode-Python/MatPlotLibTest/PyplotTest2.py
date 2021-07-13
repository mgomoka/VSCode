from matplotlib.pyplot import *
from numpy import *

x = linspace(-5, 5, 50)
y = x**2
plot(x, y)

secondX = linspace(-10, 10, 50)
secondY = x**2
plot(secondX, secondY)

show()
