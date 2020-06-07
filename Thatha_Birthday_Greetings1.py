
import turtle

# size is a variable. Can defined by us. It an be any thing
# Input 
# varaiable name can be anything . number , charcter, float, integer
"""
cake_size = input ("Size of cake:")
cake_size=int(cake_size)
cake_layer = input ("Layers of cake:")

"""
#cake_layer3_colour = input ("Layer 1 colour red, brown , yellow, lime green, blue:")

#cake_layer2_colour = input ("Layer 2 colour red, brown , yellow, lime green, blue:")
#
#cake_layer3_colour = input ("Layer 3 colour red, brown , yellow, lime green, blue:")

#cake_layer4_colour = input ("Layer 4 colour red, brown , yellow, lime green, blue:")

#cake_layer5_colour = input ("Layer 5 colour red, brown , yellow, lime green, blue:")



t = turtle.Turtle()
t.fillcolor('blue')
t.pu()
t.goto(-300,0)
t.pd()
t.begin_fill()
for i in range(2):
  t.forward(600)
  t.right(90)
  t.forward(100)
  t.right(90)
t.end_fill()

"""

cake_size = 100

cake_size = int(cake_size)

#print (cake_size)
#print (cake_layer)
make.color("red")
make.begin_fill()
for i in range(4):

    make.forward(cake_size)
    make.right(90)
    make.forward(cake_size/2)
    print(cake_size)
    print(cake_size/2)   



make.end_fill() 
make.forward(100)
make.right(90)
make.forward(50)
make.forward(100)
make.right(90)
make.forward(100)
make.forward(50)
make.right(90)
make.forward(100)
make.forward(50)
make.right(90)
make.forward(100)

"""