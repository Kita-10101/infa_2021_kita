print('Исполнитель "Черепаха" (ч.1)')
print('Использование циклов for, вложенных циклов, функций')
print('Упражнение №11: "бабочка"')
import turtle
n = int(input())
turtle.shape('turtle')
turtle.left(90)
for k in range(n):
    for i in range(180):
        turtle.forward(0.5 + 0.2 * k)
        turtle.left(2)
    for j in range(180):
        turtle.forward(0.5 + 0.2 * k)
        turtle.right(2)
print()
