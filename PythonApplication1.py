
import turtle


cake = turtle.Turtle() #creation of objet
cakescreen = turtle.Screen()

cakescreen.bgcolor("#FFF8D5")
v=input()
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

cake.fillcolor('#ffff00')
cake.begin_fill()
cake.forward(100)
cake.left(90)
for i in range(2):

 cake.forward(100)
 cake.right(90)
 cake.forward(400)
 cake.right(90) 
cake.end_fill()


cake.fillcolor('#03e700')
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

cake.fillcolor('white')   #color fill
cake.pu()                #pen up
cake.goto(-300,-250)        #turtle go back
cake.pd()                #pen down
cake.begin_fill()        #will begin fill
for i in range(2):      #will do same comand two times
  cake.forward(600)     # turtle will 600 steps forward
  cake.right(90)
  cake.forward(25)
  cake.right(90)        # turtle will turn 90 degree
cake.end_fill()

cake.fillcolor('white')
cake.pu()
cake.goto(-200,-150)
cake.pd()
cake.begin_fill()

for i in range(2):
 cake.forward(400)
 cake.right(90) 
 cake.forward(25)
 cake.right(90)

cake.end_fill()


cake.fillcolor('white')
cake.pu()
cake.goto(-100,-50)
cake.pd()
cake.begin_fill()

for i in range(2):
 cake.forward(200)
 cake.right(90)
 cake.forward(25)
 cake.right(90) 
cake.end_fill()

cake.fillcolor("red")
for i in range(5):

 cake.pu()
 cake.goto((-85+(40*i)),-70)
 cake.pd()

 cake.begin_fill()
 cake.circle(7)
 cake.end_fill()
for i in range(10):

 cake.pu()
 cake.goto((-185+(40*i)),-170)
 cake.pd()

 cake.begin_fill()
 cake.circle(7)
 cake.end_fill()
for i in range(15):

 cake.pu()
 cake.goto((-285+(40*i)),-270)
 cake.pd()

 cake.begin_fill()
 cake.circle(7)
 cake.end_fill()

cake.pu()
cake.goto(-95,-50)
cake.pd()
cake.lt(90)
cake.fillcolor("#fff2a5")
cake.begin_fill()
for i in range(2):
    cake.fd(80)
    cake.rt(90)
    cake.fd(20)
    cake.rt(90)
cake.pu()
cake.goto(75,-50)
cake.pd()
cake.end_fill()
cake.begin_fill()
for i in range(2):
    cake.fd(80)
    cake.rt(90)
    cake.fd(20)
    cake.rt(90)
cake.end_fill()
cake.fillcolor("#ff6600")
cake.pu()
cake.goto(-75,43)
cake.pd()
cake.begin_fill()
cake.circle(12)
cake.end_fill()
cake.pu()
cake.goto(95,43)
cake.pd()
cake.begin_fill()
cake.circle(12)
cake.end_fill()




cake.hideturtle()
cake.pu()                #pen up
cake.goto(0,250)        #turtle go back
cake.pd()                #pen down


cake.pencolor("#03e700")
cake.write("Happy Birthday Thatha", move=True, align="center", font=("Comic Sans MS", 50, "italic"))

cake.pu()        #pen up
cake.goto(-50,-50)        #turtle go back
cake.pd()                #pen down

cake.write("8", move=True, align="left", font=("Comic Sans MS", 70, "normal"))
cake.write("2", move=True, align="left", font=("Comic Sans MS", 70, "normal"))

cake.pu()
cake.goto(-300,200)
cake.pd()


cake.pu()
cake.goto(-300,170)
cake.pd()
cake.write("Pugazh", move=True, align="left", font=("Comic Sans MS", 15, "italic"))
cake.pu()
cake.goto(-300,140)
cake.pd()
cake.pencolor("#ff5500")
cake.write("Madhen", move=True, align="left", font=("Comic Sans MS", 15, "italic"))
cake.pu()
cake.goto(-300,110)
cake.pd()
cake.pencolor("#00e2cd")
cake.write("Sembiyan", move=True, align="left", font=("Comic Sans MS", 15, "italic"))
cake.pu()
cake.goto(-300,80)
cake.pd()
cake.pencolor("#ff02b9")
cake.write("Aathirai", move=True, align="left", font=("Comic Sans MS", 15, "italic"))
cake.pu()
cake.goto(300,170)
cake.pd()
cake.pencolor("#ff0000")
cake.write("Kappiyan", move=True, align="left", font=("Comic Sans MS", 15, "italic"))
cake.pu()
cake.goto(300,140)
cake.pd()
cake.pencolor("#0037cd")
cake.write("Kabilan", move=True, align="left", font=("Comic Sans MS", 15, "italic"))
cake.pu()
cake.goto(300,110)
cake.pd()
cake.pencolor("#7e00ff")
cake.write("Elakkiyan", move=True, align="left", font=("Comic Sans MS", 15, "italic"))



x=input()



