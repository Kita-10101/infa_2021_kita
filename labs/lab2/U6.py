print('Исполнитель "Черепаха" (ч.1)')
print('Использование циклов for, вложенных циклов, функций')
print('Упражнение №6: паук')
n = int(input())
import turtle
turtle.shape('turtle')
turtle.right(360 / (n * 2))
for i in range(n):
    turtle.forward(100)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(100)
    turtle.right(180 + 360 / n)
print()
