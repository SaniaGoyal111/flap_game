import pygame
import random

pygame.init()
SCREEN= pygame.display.set_mode((500,750))

BACKGROUND_image= pygame.image.load('background.png')
background_image = pygame.transform.scale(BACKGROUND_image, (500,750))

Bird_image=pygame.image.load("bird.png")
Bird_image = pygame.transform.scale(Bird_image, (64,64))
bird_x= 50
bird_y= 300
bird_y_change= 0

def display_bird(x,y):
    SCREEN.blit(Bird_image, (x,y))

#obstacles
obstacle_width = 70
obstacle_height =random.randint(150,450)
obstacle_color = (211,253,117)
obstacle_x_change = -0.15
obstacle_x= 500
gap= 200

def display_obstacle(x,height):
    pygame.draw.rect(SCREEN, obstacle_color,(x,0,obstacle_width,height))
    bottom_obstacle_height = 750 -height - gap
    pygame.draw.rect(SCREEN, obstacle_color,(x,750 - bottom_obstacle_height,obstacle_width,bottom_obstacle_height))

def collision_detection(obstacle_x,obstacle_height,bird_y,gap):
    if obstacle_x >=50 and obstacle_x <= (50+64):
        if bird_y <= obstacle_height or bird_y >= (obstacle_height + gap -64):
            return True
    return False 

score= 0

def score_display(score):
    display=SCORE_FONT.render(f"Score: {score}" , True , (255,255,255))
    SCREEN.blit(display,(10,10))

running= True
while running:
    SCREEN.fill((0,0,0))
    SCREEN.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # space_pressed = True
                bird_y_change = -0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 0.1 

    bird_y += bird_y_change
    if bird_y <=0:
        bird_y = 0
    if bird_y >= 686:
        bird_y = 686
    obstacle_x += obstacle_x_change
    if obstacle_x <= -obstacle_width:
        obstacle_x= 500
        obstacle_height=random.randint(150,450)
        score +=1

    display_obstacle(obstacle_x,obstacle_height) 

    collision= collision_detection(obstacle_x, obstacle_height, bird_y ,gap)
   
    if collision:
       running =False
   
    display_bird(bird_x, bird_y) 

    pygame.display.update()
   
pygame.quit()
print("your score is ", score)