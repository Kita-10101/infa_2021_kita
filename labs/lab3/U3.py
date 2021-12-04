print('Исполнитель "Черепаха" (ч.2)')
print('Ветвления, функции, декомпозиция')
print('Упражнение №3')
import turtle
vvod = open('U3_text', 'r')
s = vvod.read().split()
print(s)
p = input()
b = int(input())
turtle.shape('turtle')
turtle.color('red')
turtle.width(3)
turtle.speed(1)

def number(point, a):
    x = turtle.xcor()
    y = turtle.ycor()
    if point == '0':
        turtle.penup()
        y = y - a
        turtle.goto(x, y)
        turtle.pendown()
    elif point == '1':
        x = x + a
        turtle.goto(x, y)
    elif point == '2':
        y = y - a
        turtle.goto(x, y)
    elif point == '3':
        x = x - a
        turtle.goto(x, y)
    elif point == '4':
        y = y + a
        turtle.goto(x, y)
    elif point == '5':
        x = x - a
        y = y - a
        turtle.goto(x, y)
    elif point == '6':
        x = x + a
        y = y + a
        turtle.goto(x, y)
    elif point == '7':
        turtle.penup()
        turtle.goto(0, 0)
        x = 2 * (i + 1) * a
        y = 0
        turtle.goto(x, y)
        turtle.pendown()

for i in range(len(p)):
    for j in range(len(s[int(p[i])])):
        number(s[int(p[i])][j], b)

out = open('output.txt', 'w')
print()
