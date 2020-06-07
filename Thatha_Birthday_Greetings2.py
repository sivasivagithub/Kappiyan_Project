
import turtle
make = turtle.Pen()

#size=input("Size of cake:")
size=100
size=int(size)
#layer=input("How many layers:")
#layer = int(layer)

"""
for i in range(layer):
 if (size<=size*layer): 
  make.forward(size)
  make.right(90)
  make.forward(size/2)
  make.left(90)
  print(i)
 
make.right(180)
make.forward(size*layer*2)
make.right(90)
for i in range(layer):
 if (size<=size*(layer-1)): 
  make.forward(size/2)
  make.right(90)
  make.forward(size)
  make.left(90)
  print(i)
print("Happy BirthDay")

"""



turtle.home()
turtle.position()
(3000.00,500000.00)

for i in range(4):

  make.forward(size)
  make.right(90)
  make.forward(size/2)
  make.right(90)
  print(i)
print("Happy BirthDay")

