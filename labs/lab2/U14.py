print('Исполнитель "Черепаха" (ч.1)')
print('Использование циклов for, вложенных циклов, функций')
print('Упражнение №14: звёзды')
import turtle
n = int(input())
turtle.shape('turtle')
turtle.goto(0, 0)
for i in range(n):
    turtle.forward(100)
    turtle.left(180 - 180 / n)
if n % 2 == 0:
    turtle.goto(0, 0)
print()
