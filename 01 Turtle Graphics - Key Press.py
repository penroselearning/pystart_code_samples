# Concepts to be learned
# Adding Images
# Registering an Image as a Movable Object
# Enable Keyboard Movements

import turtle

screen = turtle.Screen()

# this assures that the size of the screen will always be 800x500 ...
screen.setup(800, 500)

# ... which is the same size as our image
# now set the background to our space image
screen.bgpic("clearsky.png")

# Or, set the shape of a turtle
screen.addshape("helicopter.gif")
turtle.shape("helicopter.gif")

move_speed = 10
turn_speed = 10

# these defs control the movement of our "turtle"
# We will learn about creating our own defs in Future Lessons
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
turtle.setpos(-200,100)

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
screen.mainloop()