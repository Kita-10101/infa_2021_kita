print('Исполнитель "Черепаха" (ч.1)')
print('Использование циклов for, вложенных циклов, функций')
print('Упражнение №8: квадратная "спираль"')
import turtle
turtle.shape('turtle')
for j in range(20):
    for i in range(2):
        turtle.forward(10 + j * 10)
        turtle.left(90)
print()
