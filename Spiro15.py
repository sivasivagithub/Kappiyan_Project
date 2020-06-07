
from turtle import *
from random import randint
bgcolor('black')
x = 1
speed(100)
while x < 249:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    print (x)
    print(x)
    print(x)
    colormode(255)
    x=x+1
    pencolor(x+3, x+5, 255-x)
    bgcolor(255 , 255 , 255-x)
    k = color()
    #fd(50 + x)
    #rt(90.991)
    x = x + 1
    print(k)

k = input("Hit enter")