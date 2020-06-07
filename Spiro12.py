
import turtle

t = turtle.Turtle()

t.pensize(2)
t.speed(200)
t.color("Green")
turtle.bgcolor("#FF9999")

#na = 000000" +000001

#print (na)

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

tp = t.pos()
print (tp)

k = input("Hit enter")



