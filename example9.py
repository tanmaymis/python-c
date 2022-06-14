from turtle import *
color = ['purple','green', 'blue', 'red']

pencolor(color[0])
penup()
goto(-200,150)
pendown()
for i in range(4):
    fd(50)
    lt(90)
pencolor(color[1])
penup()
goto(200,150)
pendown()
for i in range(4):
    fd(50)
    lt(90)
pencolor(color[2])
penup()
goto(-200,-150)
pendown()
for i in range(4):
    fd(50)
    lt(90)
pencolor(color[3])
penup()
goto(200,-150)
pendown()
for i in range(4):
    fd(50)
    lt(90)

mainloop()