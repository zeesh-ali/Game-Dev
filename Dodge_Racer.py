# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 02:35:03 2017

@author: Zeeshan
"""

import pygame
import time
import random
#Initiate pygame
pygame.init()

#Screen Size
display_width=640
display_height=480

#pixel width of car
car_width=110

#Defining Colors in RGB
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)


#Set Mode specifying screen size and depth for the screen
screen = pygame.display.set_mode((display_width,display_height),0,32)

#Caption of the window
pygame.display.set_caption('Racer')

#
clock=pygame.time.Clock()

#Sprite Image of my car
carImg=pygame.image.load('racer.png')

#Function returning text and a rectangle around text so that it can be placed
#in the middle of the screen later
def text_objects(text,font_text):
    textSur=font_text.render(text,True,black)
    return textSur,textSur.get_rect()

#This function is called when car crashes, message passed to be displayed here
def crashed():
    message_display('Kaboom!!!')

#Function to display message in a particular font and size
#Centering the message in the middle of screen
#Sleep for 2 sec on displaying message
#Restart game
def message_display(text):
    font_text=pygame.font.SysFont('arial',115)
    TextSurf,TextRect=text_objects(text,font_text)
    TextRect.center=((display_width/2),(display_height/2))
    screen.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    
    game_loop()
 
#To update the image of car according to x and y co-ordinates    
def car(x,y):
    screen.blit(carImg,(x,y))       

#Draw rectangle box        
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(screen,color,[thingx,thingy,thingw,thingh])

#Score counter
def things_dodged(count):
    font=pygame.font.SysFont('none',25)
    text=font.render('Score: '+str(count),True,blue)
    screen.blit(text,(0,0))

#Game loop function
#Key event handling and operations
#Generating boxes and dropping logic
def game_loop():
    #Initial Position of Car
    x=(display_width*0.45)
    y=(display_height*0.8)
    
    #Initializing x,y coordinates
    x_change=0
    y_change=0
    gameExit= False
    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=7
    thing_height=100
    thing_width=100
    
    score=0

        
    #Game Loop
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                quit() #Quit python    
            if event.type == pygame.KEYDOWN: #Key Event Handling
                if event.key == pygame.K_LEFT:
                    x_change=-5
                if event.key== pygame.K_RIGHT:
                    x_change=+5
                if event.key== pygame.K_UP:
                    y_change=-5
                if event.key== pygame.K_DOWN:
                    y_change=+5
                    
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_DOWN]: y += 5
            if pressed[pygame.K_UP]: y -= 5
            if pressed[pygame.K_LEFT]: x -= 5
            if pressed[pygame.K_RIGHT]: x += 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change=0
        
        x=x+x_change            
        y=y+y_change    
        screen.fill(white)
        #things(thingx,thingy,thingw,thingh,color)
        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty=thing_starty+thing_speed
        car(x,y)
        things_dodged(score)
        
        #Wall collision logic
        if x> display_width-car_width or x<0:
            crashed()
            
        #Score Logic
        if thing_starty>display_height:
            thing_starty=0
            thing_startx=random.randrange(0,display_width)
            score+=1
            
        #object Collision logic    
        if y<thing_starty+thing_height and thing_startx<x+car_width and thing_startx+thing_width>x:
            crashed()
            
        pygame.display.update()
        clock.tick(30) #Frame per second

#Calling gmae_loop funciton
game_loop()
pygame.quit() #quit pygame
quit() #Quit python    