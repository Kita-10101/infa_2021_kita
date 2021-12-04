print('Исполнитель "Черепаха" (ч.1)')
print('Использование циклов for, вложенных циклов, функций')
print('Упражнение №9: правильные многоугольники')
import turtle
from math import pi, sin
turtle.shape('turtle')
def polygon(n, r):
    turtle.right(180)
    turtle.right(90 * (n-2) / n)
    for i in range(n):
        turtle.forward(r)
        turtle.left(180)
        turtle.right(180 * (n - 2) / n)
    turtle.penup()
r = 20
n = 3
turtle.goto(0, 0)
for i in range(10):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.forward(0.5 * r / sin(pi / n))
    turtle.pendown()
    polygon(n, r)
    r = r + 10
    n = n + 1
print()
