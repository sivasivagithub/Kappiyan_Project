
import turtle
make = turtle.Pen()

size=input("Size of cake:")
size=int(size)
layer=input("How many layers:")
layer = int(layer)
listColor=["Red","Orange","Lime Green","Blue","Yellow"]
print("Choose the color of each layer from these values:",listColor[0:5])
layerColor=list(range(layer))
color=list(range(1))

for i in range(layer):
    print("Input color of",(i+1))
    color[0]=input()
    check=any(x in listColor for x in color)
    layerColor[i]=color[0]

for i in range(layer):
 if (size<=size*layer): 
  make.pencolor(layerColor[i])
  make.fd(size)
  make.rt(90)
  make.fd(size/2)
  make.rt(90)
  make.goto(0,-((size/2)*(i+1))) 
  make.pu()
  make.bk(size*(i+1))
  make.pd()
  make.lt(180)

make.bk(size*layer*2)
make.lt(90)
f=int(layer-1)
l=int(layer-2)
make.fillcolor(layerColor[f])
for i in range(layer):
  if (size<=size*(layer-1)): 
   make.fd(size/2) 
   make.pencolor(layerColor[l])
   make.fillcolor(layerColor[f])
   make.rt(90)
   make.goto(0,-((size/2)*f))
   make.pu() 
   make.bk(size*(f))
   make.pd()
   make.lt(90)
   f=f-1
   l=l-1

print("Happy BirthDay")
