
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(2000)

t = turtle.Turtle()

t.color("green")

# radius for smallest circle
r = 10

# number of circles
n = 10

# loop for printing tangent circles
for i in range(1, n + 1, 1):
    t.circle(r * i)


  