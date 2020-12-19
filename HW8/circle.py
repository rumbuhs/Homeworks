import pygame
 
FPS = 60
DISPLAY_WIDTH = 700 # ширина екрана
DISPLAY_HEIGH = 300 # висота екрана
  
WHITE_COLOR = (255, 255, 255)
BLUE_COLOR = (0, 70, 225)
 

# координати і радіус круга
COORD_X = DISPLAY_WIDTH // 2
COORD_Y = DISPLAY_HEIGH // 2
RADIUS = 50

pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

pygame.display.set_caption("My second game")

clock = pygame.time.Clock()
 
while True:
    screen.fill(WHITE_COLOR)
 
    pygame.draw.circle(screen, BLUE_COLOR, (COORD_X, COORD_Y), RADIUS)
 
    pygame.display.update()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
         
    clock.tick(FPS)