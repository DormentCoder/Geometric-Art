# Geometric Art
# by Dc117 Corp.

import turtle
from random import*

turtle.penup()
turtle.goto(randint(-1000,0), randint(-1000,1000))
turtle.fillcolor("Yellow")
turtle.begin_fill()
turtle.pendown()
side = randint(100,1000)
for i in range(0,4):
    turtle.forward(side)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
for rectangle in range(1,11):
  turtle.setheading(randint(0,90))
  turtle.penup()
  turtle.goto(randint(-2000,1000),randint(-2000,1000))
  turtle.fillcolor("Blue")
  turtle.begin_fill()
  turtle.pendown()
  length = randint(500,1500)
  width = randint(100, length)
  for i in range(0,2):
      turtle.forward(length)
      turtle.left(90)
      turtle.forward(width)
      turtle.left(90)
  turtle.end_fill()
  turtle.penup()
for triangle in range(1,11):
  turtle.setheading(randint(0,90))
  turtle.penup()
  turtle.goto(randint(-1000,1000),randint(0,1000))
  turtle.fillcolor("Red")
  turtle.begin_fill()
  turtle.pendown()
  side = randint(100,1000)
  for i in range(0,3):
      turtle.forward(side)
      turtle.left(120)
  turtle.end_fill()
  turtle.penup()
turtle.goto(35, 55)
turtle.fillcolor("Black")
turtle.begin_fill()
turtle.circle(8)
turtle.end_fill()
turtle.penup()
turtle.hideturtle()