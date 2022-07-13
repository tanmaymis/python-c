import pgzrun

HEIGHT =500
WIDTH =600

item =Rect((300,350),(25,25))
ivy =5
item2 = Rect((250,250),(25,25))
i2vy=6
item3 = Rect((400,150),(25,25))
i3vy=4
platform =Rect((WIDTH-25,HEIGHT-250),(10,80))
platform2 =Rect((WIDTH-25,HEIGHT-250),(460,80))


def item_motion_control(obj,plt,speed): #parameters

    obj.x +=speed
    if obj.x> HEIGHT:
        obj.x =0
    if obj.x<0:
        obj.x =0
        speed = -speed
    if obj.colliderect(plt):
        speed =- speed
    return speed
    
def platform_control():
    if keyboard.left:
        platform.x -= 3
    if keyboard.right:
        platform.x += 3
    if keyboard.left:
        platform2.x -= 3
    if keyboard.right:
        platform2.x += 3


def draw():
    screen.fill('white')
    screen.draw.filled_rect(item, 'green')
    screen.draw.filled_rect(item2, 'red')
    screen.draw.filled_rect(item3, 'blue')
    screen.draw.filled_rect(platform, 'brown')
    screen.draw.filled_rect(platform2, 'brown')

def update():
    global ivy
    global i2vy
    global i3vy
    ivy = item_motion_control(item,platform,ivy)
    i2vy = item_motion_control(item2,platform,i2vy)
    i3vy = item_motion_control(item3,platform,i3vy)
    #keyboard control
    platform_control()

    print(item.x, item.y,ivy)

pgzrun.go()