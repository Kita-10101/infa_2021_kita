print('Исполнитель "Черепаха" (ч.1)')
print('Использование циклов for, вложенных циклов, функций')
print('Упражнение №5: больше квадратов')
import turtle
turtle.shape('turtle')
for j in range(10):
    for i in range(4):
        turtle.forward(25 + j * 20)
        turtle.left(90)
    turtle.penup()
    turtle.goto(-(10 + j * 10), -(10 + j * 10))
    turtle.pendown()
print()
