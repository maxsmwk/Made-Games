import pygame 

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("test game")

clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 50)
text_surface = test_font.render("Hello World", False, "Red")
example_button = pygame.image.load("Game 1/graphics/buttonsprites/exbutton.png")
wooden_floor = pygame.image.load("Game 1/graphics/scenes/woodenfloor.png")

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(example_button, (200,100))
    screen.blit(wooden_floor, (400,0))
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()