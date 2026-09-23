import pygame 

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("test game")

clock = pygame.time.Clock()

class Button:
    def __init__(self, image, ):
        self.image = pygame.image.load(image).convert_alpha()

    def draw(self, x, y):
        screen.blit(self.image, (x,y))

example_button = Button("Game 1/graphics/buttonsprites/exbutton.png")

        

test_font = pygame.font.Font("Game 1/graphics/textfonts/HARRYP__.TTF", 50)
text_surface = test_font.render("Hello World", False, "Red")
wooden_floor = pygame.image.load("Game 1/graphics/scenes/woodenfloor.png")
snail_surface = pygame.image.load("Game 1/graphics/charactersprites/snail/snail1.png")
snail_x_pos = 600
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    example_button.draw(200, 50)
    screen.blit(wooden_floor, (400,0))
    screen.blit(text_surface, (300, 50))
    if snail_x_pos > 800:
        snail_x_pos = 600
    screen.blit(snail_surface, (snail_x_pos, 40))
    snail_x_pos += 1


    pygame.display.update()
    clock.tick(60)

pygame.quit()