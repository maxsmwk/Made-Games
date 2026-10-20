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
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()


    def draw(self, x, y):
        self.rect.center = (x, y)
        screen.blit(self.image, self.rect)

    def draw_rect_top_left(self, x, y, color = "Red"):
        self.rect.topleft = (x, y)
        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.image, self.rect)

    def draw_rect_bottom_left(self, x, y, color = "Red"):
        self.rect.bottomleft = (x, y)
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

def procedural_generate():
    
    #GENERATE ON SCREEN RANDOM
    uganda_knuckles_upper = Sprite(uganda_knuckles_file, scale)
    uganda_knuckles_lower = Sprite(uganda_knuckles_file, scale)
    gap_width = uganda_knuckles_upper.width * scale
    gap_rect = pygame.rect.Rect((gap_x_pos, gap_y_pos), (gap_width, gap_height1))
    gap_rect.midleft = (gap_x_pos, gap_y_pos)

    #GAP RECT POSITIONS
    gap_rect_bottomleft_x = gap_rect.bottomleft[0]
    gap_rect_bottomleft_y = gap_rect.bottomleft[1]
    gap_rect_topleft_x = gap_rect.topleft[0]
    gap_rect_topleft_y = gap_rect.topleft[1]
    
    #DRAW BOTTOM
    uganda_knuckles_lower.draw_rect_top_left(gap_rect_bottomleft_x, gap_rect_bottomleft_y)
    
    #DRAW TOP
    uganda_knuckles_upper.draw_rect_bottom_left(gap_rect_topleft_x, gap_rect_topleft_y)


    


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
play_again_button_file = "flappy chungus/Graphics/Buttons/playagain.png"
play_again_button = Button(play_again_button_file)

#SPRITES
city_background_file = "flappy chungus/Graphics/Sprites/citybackground.jpg"
city_background = Sprite(city_background_file, 3.1)

uganda_knuckles_file = "flappy chungus/Graphics/Sprites/ugandaknucklessprite.png"

#SPRITE CONSTANTS
gap_x_pos = SCREEN_WIDTH/2
gap_y_pos = SCREEN_HEIGHT/2


#Player
big_chungus_pixel_file = "flappy chungus/Graphics/Sprites/pixelbigchungussprite.png"
big_chungus_pixel = pygame.image.load(big_chungus_pixel_file).convert_alpha()
big_chungus_pixel_width = big_chungus_pixel.get_width()
big_chungus_pixel_height = big_chungus_pixel.get_height()
scale = .2
big_chungus_pixel = pygame.transform.scale(big_chungus_pixel, ((big_chungus_pixel_width * scale), (big_chungus_pixel_height * scale)))
big_chungus_pixel_rect = big_chungus_pixel.get_rect()
big_chungus_pixel_rect.center = (50, SCREEN_HEIGHT/2)
PLAYER_GRAV = 0

#procedural generate FIRST OBST
obstacle_gap_lower1 = big_chungus_pixel_rect.height + 30
obstacle_gap_higher1 = big_chungus_pixel_rect.height + 400
top_limit  = 50
bottom_limit = SCREEN_HEIGHT
gap_y_pos1 = random.randint(top_limit, bottom_limit)
gap_height1 = random.randint(obstacle_gap_lower1, obstacle_gap_higher1)
scale = random.randint(3,10)
scale /= 10 


#FONTS
hp_font = Font("flappy chungus/Graphics/Text/PermanentMarker-Regular.ttf", 50)

#CONDITIONS
game_active = False
if_play = False
game_over = False
menu_active = True
run = True

while run:


    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            #PLAY CLICK
            if play_button.rect.collidepoint(event.pos):
                menu_active = False
                if_play = True
            #PLAY AGAIN
            if play_again_button.rect.collidepoint(event.pos):
                game_over = False
                game_active = False
                if_play = True

    #MENU
    if menu_active:
        menu()

    #BEFORE GAME ACTIVE
    if if_play:
    #KEYBOARD INPUT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if_play = False
            game_active = True
    #BG
        city_background.draw(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        hp_font.messagedraw("Space To Begin", SCREEN_WIDTH/2, 100)
    if game_active:

        #KEYBOARD INPUT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            PLAYER_GRAV = -10


        screen.fill("Black")

        #BG
        city_background.draw(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        #OBSTACLES
        procedural_generate()
        gap_x_pos1 -= 4

        #PLAYER
        PLAYER_GRAV += 1
        big_chungus_pixel_rect.y += PLAYER_GRAV
        if big_chungus_pixel_rect.bottom > SCREEN_HEIGHT:
            game_over = True
        elif big_chungus_pixel_rect.top < 50:
            big_chungus_pixel_rect.top = 50
        screen.blit(big_chungus_pixel, big_chungus_pixel_rect)

    if game_over:
        screen.fill((60, 130, 200))
        PLAYER_GRAV = 0
        big_chungus_pixel_rect.center = (50, SCREEN_HEIGHT/2)
        play_again_button.draw(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        hp_font.messagedraw("Game Over...", SCREEN_WIDTH/2, 100)

    #DISPLAY UPDATE
    pygame.display.update()

    #FRAMERATE
    clock.tick(60)

pygame.quit()

