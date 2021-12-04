print('Исполнитель "Черепаха" (ч.1)')
print('Использование циклов for, вложенных циклов, функций')
print('Упражнение №12: пружина')
import turtle
n = int(input())
turtle.shape('turtle')
turtle.left(90)
for j in range(n):
    for i in range(180):
        turtle.forward(0.5)
        turtle.right(1)
    for i in range(18):
        turtle.forward(0.5)
        turtle.right(10)
print()
