# pygame.init()
# screen = pygame.display.set_mode((400,400))
# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 18)
 
 
# def update_fps():
# 	fps = str(int(clock.get_fps()))
# 	fps_text = font.render(fps, 1, pygame.Color("coral"))
# 	return fps_text
 
 
# loop = 1
# while loop:
# 	screen.fill((0, 0, 0))
# 	screen.blit(update_fps(), (10,0))
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			loop = 0
# 	clock.tick(60)
# 	pygame.display.update()
 
# pygame.quit()

####################################################
import pygame
pygame.init()
screenwidth = 500
screenheight = 500
screen = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)



def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text


pygame.display.set_caption("First Game")

#Variables for game 
x = 50 #position
y = 50 #position
width = 40 #size of rectangle
height = 60 #size of rectangle
vel = 5 #movement steps

run = True

while run:
    pygame.time.delay(50)

    #check if the close button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < (screenwidth - width - vel):
        x += vel
    if keys[pygame.K_UP] and y > vel: 
        y -= vel
    if keys[pygame.K_DOWN] and y < (screenheight - height - vel):
        y += vel

    screen.fill((0,0,0)) #fill the screen with black
    pygame.draw.rect(screen, (255, 0, 0), (x,y,width,height))
    pygame.display.update()

pygame.quit()