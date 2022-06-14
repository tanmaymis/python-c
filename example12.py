from turtle import *

s = Screen()
s.setup(800,800)
s.bgcolor('black')
speed('fastest')
pencolor('yellow')
for i in range(10):
    lt(36)
    for i in range(5):
        fd(100)
        rt(144)
mainloop()