import turtle
import random

turtleName = turtle.Turtle()
turtle.bgcolor("black")
turtle.colormode(255)
turtle.bgcolor(0,100,0)
turtle.speed(1)

for i in range (10):
 R = random.randint(1, 255)
 B = random.randint(1, 255)
 G = random.randint(1, 255)

 turtle.bgcolor(R,B,G)
 k = input("Hit enter")

print("R =" )
print(R)
print("B =" )

print(B )
print("G =" )
print(G )
    #turtle.circle(100,180,1)
   # turtle.setposition(5+i,5+i)


#turtle.bgcolor("Black")
#turtle.bgcolor(234,1,210)
#for i in range (10):
 #   turtle.bgcolor(255-i,1+i,210)


print("end")

k = input("Hit enter")

#for i in range (10):
#turtle.bgcolor(255-i,1+i,210)
