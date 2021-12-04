print('Исполнитель "Черепаха" (ч.1)')
print('Использование циклов for, вложенных циклов, функций')
print('Упражнение №10: "цветок"')
import turtle
turtle.shape('turtle')
for k in range(3):
    for i in range(360):
        turtle.forward(0.5)
        turtle.left(1)
    for j in range(360):
        turtle.forward(0.5)
        turtle.right(1)
    turtle.left(60)
print()
