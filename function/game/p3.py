import pgzrun

HEIGHT =500
WIDTH =600

item =Rect((300,250),(25,25))
ivy =5
item2 = Rect((250,250),(25,25))
i2vy=6
item3 = Rect((400,250),(25,25))
i3vy=7
platform =Rect((WIDTH/2-250/2,HEIGHT-50),(250,25))


def item_motion_control(obj,plt,speed): #parameters

    obj.y +=speed
    if obj.y> HEIGHT:
        obj.y =0
    if obj.y<0:
        obj.y =0
        speed = -speed
    if obj.colliderect(plt):
        speed =- speed
    return speed
def platform_control():
    if keyboard.left:
        platform.x -= 3
    if keyboard.right:
        platform.x += 3


def draw():
    screen.fill('white')
    screen.draw.filled_rect(item, 'green')
    screen.draw.filled_rect(item2, 'red')
    screen.draw.filled_rect(item3, 'blue')
    screen.draw.filled_rect(platform, 'brown')

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


