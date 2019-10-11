import turtle
t=turtle.Turtle()
t.width(1)
t.speed(0)
t.hideturtle()

# Body of the School Bus
t.penup()
t.setpos(-70,-100)
t.pendown()
t.begin_fill()
t.fillcolor('yellow')
t.forward(300)
t.left(90)
t.forward(200)
t.left(90)
t.forward(300)
t.left(90)
t.forward(200)
t.end_fill()

# Drivers seat
t.pu()
t.setpos(-70,100)
t.setheading(180)
t.pd()
t.begin_fill()
t.fillcolor('alice blue')
t.circle(175,75)
t.left(105)
t.forward(170)
t.left(90)
t.forward(130)
t.end_fill()
t.pu()
t.setpos(-70,-100)
t.pd()
t.begin_fill()
t.fillcolor('yellow')
for x in range(2):
    t.forward(70)
    t.left(90)
    t.forward(170)
    t.left(90)
t.end_fill()


# Right Wheel & Left Wheel
x = 160
y= -100
for wheel in range(2):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor('black')
    t.circle(50)
    t.left(0)
    t.end_fill()
    t.penup()
    t.setpos(x-40,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor('white')
    t.circle(10)
    t.left(0)
    t.end_fill()
    x = -120


# Three Windows

t.penup()
t.setpos(190,80)
t.pendown()
t.begin_fill()
t.fillcolor('alice blue')
t.setheading(180)

for windows in range(3):
    for x in range(4):
        t.forward(70)
        t.left(90)
    t.pu()
    t.forward(80)
    t.pd()
t.end_fill()

# School Bus Label
t.penup()
t.setpos(0,-40)
t.pendown()
t.write("School Bus",font=('Arial',25))

turtle.done()