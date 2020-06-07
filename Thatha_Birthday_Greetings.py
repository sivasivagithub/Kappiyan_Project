
import turtle
make = turtle.Pen()


size = 10. # size is a variable . Variables is to store values

# comment is used for description. that is not is not a code

#print (size)

size = 10+1

print("outside loop",size)


size = 10+2

print("outside loop",size)

size = 10+3

print("outside loop",size)

size = 10+4

print("outside loop",size)
size = 10+5

print("outside loop",size)


for i in range(5):
 size=size+1
 print("inside loop",size)








#size = input("Size of cake:")
#size=int(size)
#layer=input("How many layers:")
#layer = int(layer)
#for i in range(#):
# if (size<=size*layer): 
 # make.forward(size)
"""
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