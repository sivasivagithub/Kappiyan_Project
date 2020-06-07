
import turtle

turtle.setup(900,800)
turtle.bgcolor("green")
turtle.colormode(255)

for i in range (10):
    turtle.bgcolor(255-i,1+i,210)
    #turtle.circle(100,180,1)
   # turtle.setposition(5+i,5+i)


turtle.forward(1)
turtle.circle(-100,180)

turtle.heading()
turtle.position()
turtle.home()
turtle.position()
turtle.heading()
turtle.circle(100)

turtle.degrees(90)
turtle.radians()
#turtle.dot(500,"yellow")
print(turtle.window_height())
print(turtle.window_width())


k = input("Hit enter")