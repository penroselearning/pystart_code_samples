import turtle
window = turtle.Screen()
window.bgcolor("black")
robo = turtle.Turtle()

def build_robo(x,y,color,width,height):
  robo.begin_fill()
  robo.fillcolor(color)
  robo.penup()
  robo.setpos(x,y)
  robo.pendown()
  robo.hideturtle()
  for x in range(2):
    robo.forward(width)
    robo.right(90)
    robo.forward(height)
    robo.right(90)
  robo.end_fill()

# Head
build_robo(x=-40,y=120,color='red',width=80,height=80)
# Left Eye
build_robo(x=-20,y=100,color='black',width=10,height=10)
# Right Eye
build_robo(x=10,y=100,color='black',width=10,height=10)
# Mouth
build_robo(x=-20,y=60,color='black',width=40,height=6)
# Neck
build_robo(x=-10,y=40,color='yellow',width=20,height=20)
# Body
build_robo(x=-50,y=20,color='red',width=100,height=120)
# Left Leg
build_robo(x=-30,y=-100,color='yellow',width=20,height=80)
# Right Leg
build_robo(x=10,y=-100,color='yellow',width=20,height=80)
# Left Hand
build_robo(x=-130,y=0,color='yellow',width=80,height=20)
# Right Hand
build_robo(x=50,y=0,color='yellow',width=80,height=20)

window.mainloop()