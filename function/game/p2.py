import pgzrun

HEIGHT =500
WIDTH =600

item =Rect((300,250),(25,25))
platform =Rect((WIDTH/2-250/2,HEIGHT-50),(250,25))

ivy=3

def item_motion_control():
    global ivy

    item.y +=ivy
    if item.y> HEIGHT:
        item.y =0
    if item.y<0:
        item.y =0
        ivy = -ivy
    if item.colliderect(platform):
        ivy =- ivy
def platform_control():
    if keyboard.left:
        platform.x -= 3
    if keyboard.right:
        platform.x += 3


def draw():
    screen.fill('white')
    screen.draw.filled_rect(item, 'green')
    screen.draw.filled_rect(platform, 'brown')

def update():
    item_motion_control()
    #keyboard control
    platform_control()

    print(item.x, item.y,ivy)

pgzrun.go()


