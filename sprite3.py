import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Jumping Trump")

walkright = [pygame.image.load('right_1.png'),pygame.image.load('right_2.png'), pygame.image.load('right_3.png'), pygame.image.load('right_4.png'), pygame.image.load('right_5.png'), pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png'), pygame.image.load('left_3.png'), pygame.image.load('left_4.png'), pygame.image.load('left_5.png'), pygame.image.load('left_6.png')]

bg = pygame.image.load('bg1.jpg')

playerStand = pygame.image.load('idle.png')

clock=pygame.time.Clock()

x=50
y=425
width=60
height=71
speed=5

isJump=False
JumpCount=10

left=False
right=False
animCount=0

def drawScreen ():
    global animCount
    screen.blit(bg,(0,0))
    if animCount +1>=30:
        animCount=0
    if left:
        screen.blit(walkLeft[animCount//5],(x,y))
        animCount+=1
    elif right:
        screen.blit(walkright[animCount//5],(x,y))
        animCount+=1
    else:
        screen.blit(playerStand,(x,y))

    pygame.display.flip()

run=True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>5:
        x-=speed
        left=True
        right=False
    elif  keys[pygame.K_RIGHT] and x<500-width-5:
        x+=speed
        left=False
        right=True
    else:
        right=False
        left=False
        animCount=0
    if not (isJump):
        if keys [pygame.K_SPACE]:
            isJump=True
    else:
        if JumpCount>=-10:
            if JumpCount<0:
                y+=(JumpCount**2)/2
            else:
                y-=(JumpCount**2)/2
            JumpCount-=1
        else:
            isJump=False
            JumpCount=10
    drawScreen ()