#   Concepts to be learned
# - Understanding Movement, Distance and Angles
# - Setting the Position
# - Setting Speed, Width and Defining Shape of the Pen
# - Filling Colors into Shapes
# - Writing Text in Turtle Graphic

import turtle
window=turtle.Screen()
window.bgcolor("lightyellow")

pen=turtle.Turtle()
pen.pencolor("blue")

pen.speed(5)
pen.width(2)
pen.hideturtle()

pen.write("Center of Screen",align='center',font=('Arial',20,'bold'))

position_x = -300
position_y = 100

# Lifts the Pin before changing the location of the Pen
# Puts the Pen down before drawing the Shape
pen.penup()
pen.setpos(position_x,position_y)
pen.down()

pen.begin_fill()
pen.fillcolor('red')
for sides in range(4):
    pen.forward(200)
    pen.left(90)

pen.end_fill()
window.mainloop()
