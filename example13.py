from turtle import *
import random

s = Screen()
s.setup(500,500)
colors = ['pink', 'orange' , 'green']
speed('fastest')
for i in range(50):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    pensize(random.randint(1,3))
    pencolor(colors[random.randint(0,2)])
    radius = random.randint(10,30)
    fillcolor('lavender')
    begin_fill()
    for i in range(6):
        circle(radius)
        left(60)
    end_fill()
mainloop()
