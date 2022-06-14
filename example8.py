from turtle import *

s= Screen()
s.setup(1000,700)
color = ['purple' , 'green']
pencolor('black')
pensize(5)
speed('fastest')
for i in range(10,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(color[i%2])
    begin_fill()
    circle(20*i)
    end_fill()

mainloop()

