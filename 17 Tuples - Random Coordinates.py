# Using a Tuple to Store Random X and Y Coordinates to Draw 200 Circles on the Canvas

import turtle
import random

window = turtle.Screen()
window.bgcolor("black")

# Stores the Height and Width of the Window in different variables
width = window.window_width()
height = window.window_height()

pen = turtle.Turtle()
pen.speed(0)

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'white', 'silver', 'gold']

pen.penup()

for shapes in range(200):
    # Sets the Random Positions that the Shape should be drawn
    position = random.randint((-width // 2) + 30, (width // 2) - 30), random.randint((-height // 2) + 30,(height // 2) - 30)
    # Position is a Tuple containing the X anf Y Coordinates

    pen.setpos(position)  # Using a Tuple to pass the X and Y coordindates to the Turtle Pen

    pen.begin_fill()
    pen.fillcolor(random.choice(colors))
    pen.color(random.choice(colors))
    pen.pendown()

    pen.pendown()
    pen.circle(10)
    pen.penup()
    pen.end_fill()

window.mainloop()