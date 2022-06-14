from turtle import *

t =  Turtle()
t.speed("fast")

bgcolor('black')
t.color('white')
t.pensize(20)
for i in range(1,101,2):
    t.fd(i)
    t.lt(60)

mainloop()