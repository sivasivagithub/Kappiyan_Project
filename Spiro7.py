
import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(200)


for j in range (24): #Loop

    for spirocolor in ["red","magenta","cyan","blue","green","yellow","white"]:

        turtle.color(spirocolor)
        turtle.setposition(0,0)
        turtle.forward(200)
        turtle.left(160)
        turtle.forward(200)
        turtle.left(10)
        turtle.forward(200)
        turtle.hideturtle()  
      
k = input("Hit enter to exit")
       

""""      
try :
   
except EOFError as eofError:
 print ("programends")
 """


  