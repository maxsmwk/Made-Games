#FLAPPY CHUNGUS

import pygame
import random

#BUTTON CLASS
class Button:
    def __init__(self, image, scale = 1):
        self.image = pygame.image.load(image).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, ((width * scale), (height * scale)))
        self.rect = self.image.get_rect()


    def draw(self,x, y):
        self.rect.center = (x, y)
        screen.blit(self.image, self.rect)

#SPRITE CLASS
class Sprite:
    def __init__(self, image, scale = 1):
        self.image = pygame.image.load(image).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, ((width * scale), (height * scale)))
        self.rect = self.image.get_rect()


    def draw(self, x, y):
        self.rect.center = (x, y)
        screen.blit(self.image, self.rect)

    def draw_rect(self, color, x, y):
        self.rect.center = (x, y)
        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.image, self.rect)



#PLAYER CLASS
#class Player():
    #def __init__(self, image, scale = 1):
        #self.image = pygame.image.load(image).convert_alpha()
        #width = self.image.get_width()
        #height = self.image.get_height()
        #self.image = pygame.transform.scale(self.image, ((width * scale), (height * scale)))
        #self.rect = self.image.get_rect()
        


    #def draw(self, x, y):
        #self.rect.center = (x, y)
        #screen.blit(self.image, self.rect)



#FONT CLASS
class Font:
    def __init__(self, font, size):
        self.font = pygame.font.Font(font, size)

    def messagedraw(self, message, x, y, color = "White"):
        self.surf = self.font.render(message, False, color)
        self.rect = self.surf.get_rect()
        self.rect.center = (x, y)
        screen.blit(self.surf, self.rect)


def menu():
        screen.fill((60, 130, 200))
        play_button.draw(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        hp_font.messagedraw("Flappy Chungus", SCREEN_WIDTH/2, 100)


pygame.init()

#SCREEN
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#CAPTION
pygame.display.set_caption("flappy chungus")

#CLOCK
clock = pygame.time.Clock()

#BUTTONS
play_button_file = "flappy chungus/Graphics/Buttons/playbutton.png"
play_button = Button(play_button_file, .7)

#SPRITES
city_background_file = "flappy chungus/Graphics/Sprites/citybackground.jpg"
city_background = Sprite(city_background_file, 3.1)

uganda_knuckles_file = "flappy chungus/Graphics/Sprites/ugandaknucklessprite.png"
uganda_knuckles = Sprite(uganda_knuckles_file, .5)

#Player
big_chungus_pixel_file = "flappy chungus/Graphics/Sprites/pixelbigchungussprite.png"
big_chungus_pixel = pygame.image.load(big_chungus_pixel_file).convert_alpha()
big_chungus_pixel_width = big_chungus_pixel.get_width()
big_chungus_pixel_height = big_chungus_pixel.get_height()
scale = .2
big_chungus_pixel = pygame.transform.scale(big_chungus_pixel, ((big_chungus_pixel_width * scale), (big_chungus_pixel_height * scale)))
big_chungus_pixel_rect = big_chungus_pixel.get_rect()
big_chungus_pixel_rect.center = (50, SCREEN_HEIGHT/2)
PLAYER_GRAV = 1


#FONTS
hp_font = Font("flappy chungus/Graphics/Text/PermanentMarker-Regular.ttf", 50)

#LOOPS
game_active = False
menu_active = True
run = True

while run:


    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.rect.collidepoint(event.pos):
                menu_active = False
                game_active = True

    if menu_active:
        menu()

    if game_active:
        #KEYBOARD INPUT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            PLAYER_GRAV = -10


        screen.fill("Black")

        #BG
        city_background.draw(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        #OBSTACLES
        uganda_knuckles.draw_rect("Red", 1000, 700)


        #PLAYER
        PLAYER_GRAV += 1
        big_chungus_pixel_rect.y += PLAYER_GRAV
        if big_chungus_pixel_rect.bottom > SCREEN_HEIGHT:
            game_active = False
        screen.blit(big_chungus_pixel, big_chungus_pixel_rect)

    if menu_active == False and game_active == False:
        screen.fill((60, 130, 200))
        big_chungus_pixel_rect.center = (50, SCREEN_HEIGHT/2)
        hp_font.messagedraw("Game Over...", SCREEN_WIDTH/2, 100)

    #DISPLAY UPDATE
    pygame.display.update()

    #FRAMERATE
    clock.tick(60)

pygame.quit()

