import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(100)


for i in range (6):

    for spirocolor in ["red","magenta","cyan","blue","green","yellow","white"]:

        turtle.color(spirocolor)
        turtle.circle(200)
        turtle.left(10)
        turtle.hideturtle()   

      
      
        
try :
   
 k= input("Hit enter to exit")

except EOFError as eofError:

 print ("programends")



  