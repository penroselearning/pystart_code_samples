import turtle
import random
global t
global colors

turtle.bgcolor("black")
t=turtle.Pen()
t.width(5)
t.speed(5)
t.hideturtle()

colors=['red','blue','green','spring green','pink','purple','cyan','orange']

while True:
    try:
        number=int(input('What Number would you like to draw?\n'))
    except:
        print('Please type in a Whole Number')
    else:
        strnum=str(number)
        if len(strnum)<11:
            break
        else:
            print('Provide a number that is 10 digits long or less')

digits=list(strnum)

def one(x):
    t.pu()
    t.setpos(x,50)
    t.pd()
    for q in range(2):
        t.right(90)
        t.pencolor(random.choice(colors))
        t.forward(50)
        t.left(90)

def two(x):
    print()
    t.pu()
    t.setpos(x-50,50)
    t.pd()
    t.pencolor(random.choice(colors))

    for l in range(2):
        t.forward(50)
        t.right(90)
        t.pencolor(random.choice(colors))

    for l in range(2):
        t.forward(50)
        t.left(90)
        t.pencolor(random.choice(colors))

    t.forward(50)

def three(x):
    print()
    t.pu()
    t.setpos(x-50,50)
    t.pd()
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.right(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.right(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(180)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.right(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.right(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.right(180)
def four(x):
    t.pu()
    t.setpos(x-50,50)
    t.pd()
    t.right(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(180)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
def five(x):
    t.pu()
    t.setpos(x-50,50)
    t.pd()
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(180)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.right(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.right(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.right(180)
def six(x):
    t.pu()
    t.setpos(x,50)
    t.pd()
    t.right(180)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
    for q in range(4):
        t.pencolor(random.choice(colors))
        t.forward(50)
        t.right(90)
def seven(x):
    t.pu()
    t.setpos(x-50,50)
    t.pd()
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.right(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
def eight(x):
    t.pu()
    t.setpos(x-50,50)
    t.pd()
    for q in range(4):
        t.pencolor(random.choice(colors))
        t.forward(50)
        t.right(90)
    t.right(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
    for q in range(4):
        t.pencolor(random.choice(colors))
        t.forward(50)
        t.right(90)
def nine(x):
    t.pu()
    t.setpos(x,50)
    t.pd()
    t.left(180)
    for q in range (4):
        t.pencolor(random.choice(colors))
        t.forward(50)
        t.left(90)
    t.left(90)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.pencolor(random.choice(colors))
    t.forward(50)
    t.left(90)
def zero(x):
    t.pu()
    t.setpos(x-50,50)
    t.pd()
    for q in range(2):
        t.pencolor(random.choice(colors))
        t.forward(50)
        t.right(90)
        t.pencolor(random.choice(colors))
        t.forward(50)
        t.pencolor(random.choice(colors))
        t.forward(50)
        t.right(90)
def minus(x):
    t.pu()
    t.setpos(x-50,0)
    t.pd()
    t.pencolor(random.choice(colors))
    t.forward(50)

x_position=250

numcheck = {'1':one,'2':two,'3':three,'4':four,'5':five,'6':six,'7':seven,'8':eight,'9':nine,'0':zero,'-':minus}

for a in range (len(digits)):
    draw = digits[len(digits)-(a+1)]

    for d,f in numcheck.items():
        if draw == d:
            f(x_position)
    x_position-=60

turtle.done()