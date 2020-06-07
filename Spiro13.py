
import turtle

t = turtle.Turtle()

t.pensize(2)
t.speed(2)
t.color("Green")
turtle.bgcolor("#FAFF9F")

scndim = turtle.Screen()
scndim.setup(800,800)

turtle.home()

for i in range (0, 180, 30):
    print( i)
    tp = t.pos()
    print(tp)
    t.setx(i)
    t.sety(i)
    t.pendown()
    t.color("red")
    t.circle(100)
    t.penup()
print (tp)

k = input("Hit enter")



