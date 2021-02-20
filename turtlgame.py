import turtle
from random import *
from turtle import *

penup()
goto(-140,140) 

for sp in range(15): 
  speed(10)
  write(sp)
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)


turtle1 = Turtle() 
turtle1.color('green') 
turtle1.shape('turtle') 
turtle1.penup() 
turtle1.goto(-160,100) 
turtle1.pendown() 


turtle2 = Turtle() 
turtle2.color('red') 
turtle2.shape('turtle') 
turtle2.penup() 
turtle2.goto(-160,80)
turtle2.pendown() 

turtle3 = Turtle() 
turtle3.color('blue') 
turtle3.shape('turtle') 
turtle3.penup()
turtle3.goto(-160,60) 
turtle3.pendown() 

for turn in range(100): 
  turtle1.forward(randint(1,5)) 
  turtle2.forward(randint(1,5)) 
  turtle3.forward(randint(1,5)) 

turtle.done()
