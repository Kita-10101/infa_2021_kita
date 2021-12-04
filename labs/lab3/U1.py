print('Исполнитель "Черепаха" (ч.2)')
print('Ветвления, функции, декомпозиция')
print('Упражнение №1')
n = int(input())
import turtle
from random import *
turtle.shape('turtle')
turtle.color('red')
for i in range(n * 10):
    turtle.forward(random() * 50)
    if randint(0, 1) == 1:
        turtle.left(randint(0, 360))
    else:
        turtle.right(randint(0, 360))
print()
