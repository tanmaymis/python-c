from turtle import *
s=getscreen()
t=Turtle()
t.speed('fastest')
for i in range(10):
    t.fd(100)
    t.lt(60)
    t.circle(50,180)
    t.dot(20)
    
mainloop()