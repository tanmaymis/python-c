import pgzrun

HEIGHT = 500
WIDTH =500

box1 = Rect((100,250),(50,50))
box2 = Rect((10,50),(50,50))
box1_vx =2
box2_vy =3
def draw():
    screen.fill('black')
    screen.draw.text("hello world" , (10,10) ,color ="white")
    screen.draw.rect(box1,"white")
    screen.draw.filled_rect(box2 ,'red')

def update():
    global box1_vx      #to control the value of vx it can be changed
    box1.x +=2
    if box1.x > WIDTH:
        box1.x=0
    if box1.x < 0:
        box1.x=WIDTH

    global box2_vx
    box2.y +=3
    if box1.y > HEIGHT:
        box2.y=0
    if box2.y < 0:
        box2.y=HEIGHT
    if box1.colliderect(box2):
        box1_vx= -box1_vx    #- is used to change the direction
        box1_vy= -box1_vy

        print('collision')
    
pgzrun.go()