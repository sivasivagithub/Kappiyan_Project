
import turtle

t = turtle.Turtle()

t.pensize(2)
t.speed(2)
t.color("yellow")
turtle.bgcolor("green")

scndim = turtle.Screen()
scndim.setup(1400,800)

t.penup()
t.setposition(-690,-250)

tp = t.pos()
print (tp)

t.pendown()
t.left(45)
t.forward(400)
t.right(90)
t.forward(400)
t.left(90)
t.forward(400)
t.right(90)

t.forward(400)
t.right(135)
t.forward(1140)

t.penup()
t.setposition(-170,-120)
t.pendown()
t.circle(-100,)

tp = t.pos()
print (tp)

k = input("Hit enter")



