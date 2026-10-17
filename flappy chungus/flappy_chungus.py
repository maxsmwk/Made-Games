#FLAPPY CHUNGUS

import pygame

#BUTTON CLASS
class Button:
    def __init__(self, image, x, y, scale):
        self.image = pygame.image.load(image).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, ((width * scale), (height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self):
        screen.blit(self.image, self.rect)

#SPRITE CLASS
class Sprite:
    def __init__(self, image, x, y, scale):
        self.image = pygame.image.load(image).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, ((width * scale), (height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


    def draw(self):
        screen.blit(self.image, self.rect)

pygame.init()

#SCREEN
SCREEN_WIDTH = 2300
SCREEN_HEIGHT = 1200

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#CAPTION
pygame.display.set_caption("flappy chungus")

#CLOCK
clock = pygame.time.Clock()

#BUTTONS
play_button_file = "flappy chungus/Graphics/Buttons/playbutton.png"
play_button = Button(play_button_file, 800, 300, .2)
#SPRITES
big_chungus_pixel_file = "flappy chungus/Graphics/Sprites/pixelbigchungussprite.png"
big_chungus_pixel = Sprite(big_chungus_pixel_file, 300, 200, .2)

big_chungus_fancy_file = "flappy chungus/Graphics/Sprites/bigchungus fancysprit.png"
big_chungus_fancy = Sprite(big_chungus_fancy_file, 1600, 800, .2)
#LOOPS
game_active = True
run = True

while run:


    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    if game_active:
        #KEYBOARD INPUT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            pass
        if keys[pygame.K_a]:
            pass
        if keys[pygame.K_s]:
            pass
        if keys[pygame.K_w]:
            pass

        screen.fill("Black")
        big_chungus_pixel.draw()
        play_button.draw()

    #DISPLAY UPDATE
    pygame.display.update()

    #FRAMERATE
    clock.tick(60)

pygame.quit()

