print('Исполнитель "Черепаха" (ч.2)')
print('Ветвления, функции, декомпозиция')
print('Упражнение №4: физическое моделирование материальной точки')
import turtle as t
from math import sin, cos
v, a = int(input())
t.shape('square')
t.forward(v * cos(a) + 1000)
t.goto(0, 0)
