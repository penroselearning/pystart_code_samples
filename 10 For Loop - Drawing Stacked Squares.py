
# - For Loop to Draw Shapes with Turtle Graphics

import turtle
import random
window=turtle.Screen()
window.bgcolor("white")

pen=turtle.Turtle()
pen.pencolor("red")

pen.speed(0)
pen.width(2)

x=-150
y=160

pen.penup()
pen.setpos(x,y)
pen.pendown()

# Three Sets of For Loops have been stacked together to Draw 40 Squares
# Each Row has 8 Squares each

for row in range(10):       # Runs 10 Times to build the 10 Rows
  for square in range(8):   # Runs 8 Times to draw 8 Squares in Each Row
    for side in range(4):   # Runs 4 Times to draw 4 Sides of Each Square
        pen.pendown()
        pen.forward(30)
        pen.left(90)
    pen.penup()
    pen.forward(40)
  y=y-40
  pen.setpos(x,y)

window.mainloop()