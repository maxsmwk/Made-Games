import pygame 

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

flags = pygame.RESIZABLE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync = 1)

example_button = pygame.image.load("New Piskel.png").convert_alpha()

pygame.display.set_caption("test game")

green = pygame.Color.g

player = pygame.Rect(width = 50, height = 50)


run = True
while run:

    
    #draw player
    pygame.draw.rect(screen, (200, 67, 5), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print("keydown")

    pygame.display.update

pygame.quit()

