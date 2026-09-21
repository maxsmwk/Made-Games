import pygame 

pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("test game")

clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill("Red")

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()