# import turtle library
import turtle     

colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
screen = turtle.Screen()

for x in range(36):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)
   screen.clearscreen()


