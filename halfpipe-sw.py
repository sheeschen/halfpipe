# Write your code here :-)

import pgzrun
from pgzhelper import *
import random

car= Actor('halfpipe-car', pos=(100 ,100), anchor=('center', 'bottom'))

pos1 = (18,60)
pos2 = (90,140)
pos3 = (145,60)
lopos = (pos1, pos2, pos3)

WIDTH = 200
HEIGHT = 200

obplace=1
obsize=1

carplace = 2

def main():

    global obplace

    global carplace
    global obsize

    if keyboard.left:
        carplace = carplace -1
        if (carplace < 1):
            carplace = 1
    elif keyboard.right:
        carplace = carplace +1
        if (carplace > 3):
            carplace = 3


    if obsize==3 and obplace==3 and carplace ==3:
        exit()
    if obsize==3 and obplace==2 and carplace ==2:
        exit()
    if obsize==3 and obplace==1 and carplace ==1:
        exit()


    obsize=obsize+1
    if obsize>3:
        obsize=1
        obplace=random.randint(1,3)

def draw():
    screen.fill((0,0,0))
    asdf = pygame.image.load('images/background-halfpipe.png')
    new_image = pygame.transform.rotozoom(asdf, 0, 12)
    #screen.blit('background-halfpipe', (0,0))
    screen.blit(new_image, (0,0))
   # car.draw()
    parachute= pygame.image.load('images/halfpipe-car.png')
    carimage = pygame.transform.rotozoom(parachute, 0, 2)

    if carplace ==2:
        carimage = pygame.transform.rotozoom(parachute, 0, 2)
        screen.blit(carimage, (90,140))


    elif carplace ==1:
        carimage = pygame.transform.rotozoom(parachute, -90, 2)
        screen.blit(carimage, pos1)
    elif carplace ==3:
        carimage = pygame.transform.rotozoom(parachute, 90, 2)
        screen.blit(carimage, (145,60))

    #screen.blit('background-halfpipe', (0,0))



    if obsize==1:
        obimage = pygame.image.load('images/halfpipe-obstacle-1.png')
    if obsize==2:
        obimage = pygame.image.load('images/halfpipe-obstacle-2.png')
    if obsize==3:
        obimage = pygame.image.load('images/halfpipe-obstacle-3.png')


    if obplace ==2:
        ob1image = pygame.transform.rotozoom(obimage, 0, 2)
        screen.blit(ob1image, (90,140))


    elif obplace ==1:
        ob1image = pygame.transform.rotozoom(obimage, -90, 2)
        screen.blit(ob1image, pos1)
    elif obplace ==3:
        ob1image = pygame.transform.rotozoom(obimage, 90, 2)
        screen.blit(ob1image, (145,60))

    #screen.blit('background-halfpipe', (0,0))









clock.schedule_interval(main, 0.5)

