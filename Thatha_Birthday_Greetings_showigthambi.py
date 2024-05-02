
import turtle


cake = turtle.Turtle() #creation of objet
cakescreen = turtle.Screen()

cakescreen.bgcolor("#FFF8D5")


cake.fillcolor('blue')   #color fill
cake.pu()                #pen up
cake.goto(-300,-250)        #turtle go back
cake.pd()                #pen down
cake.begin_fill()        #will begin fill
for i in range(2):      #will do same comand two times
  cake.forward(600)     # turtle will 600 steps forward
  cake.right(90)
  cake.forward(100)
  cake.right(90)        # turtle will turn 90 degree
cake.end_fill()

cake.fillcolor('red')
cake.begin_fill()
cake.forward(100)
cake.left(90)
for i in range(2):

 cake.forward(100)
 cake.right(90)
 cake.forward(400)
 cake.right(90) 
cake.end_fill()


cake.fillcolor('lime green')
cake.pu()
cake.goto(-100,-50)
cake.pd()
cake.begin_fill()
cake.right(90)
for i in range(2):
 cake.forward(200)
 cake.right(90)
 cake.forward(100)
 cake.right(90) 
cake.end_fill()


cake.pu()                #pen up
cake.goto(-300,250)        #turtle go back
cake.pd()                #pen down


cake.pencolor("RED")
cake.write("Happy Birthday Kabilan", move=True, align="left", font=("Arial", 50, "normal"))

cake.pu()                #pen up
cake.goto(-50,-50)        #turtle go back
cake.pd()                #pen down

cake.write("1", move=True, align="left", font=("Arial", 70, "normal"))
cake.write("3", move=True, align="left", font=("Arial", 70, "normal"))

x= input()

