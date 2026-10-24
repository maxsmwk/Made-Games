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
        y_bottom_left = self.rect.bottomleft[1]
        if y_bottom_left < SCREEN_HEIGHT:
            self.height = SCREEN_HEIGHT - y_bottom_left
        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.image, self.rect)

    def draw_rect_bottom_left(self, x, y, color = "Red"):
        self.rect.bottomleft = (x, y)
        y_bottom_left = self.rect.topleft[1]
        if y_bottom_left > top_limit:
            self.height = y
        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.image, self.rect)
        
    def death(self):
        if self.rect.collidepoint(big_chungus_pixel_rect.center):
            return "death"










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
    
def score_display():
    current_time = pygame.time.get_ticks() - start_time
    score = current_time // 1000
    hp_font.messagedraw(str(score), SCREEN_WIDTH/2, 100)

def procedural_generate1(gap_x_pos, gap_y_pos, gap_height, scale):


        #gap rect
        gap_width = top_obstacle1.width
        gap_rect = pygame.rect.Rect((gap_x_pos, gap_y_pos), (gap_width, gap_height))
        gap_rect.midleft = (gap_x_pos, gap_y_pos)

            #GAP RECT POSITIONS
        gap_rect_bottomleft_x = gap_rect.bottomleft[0]
        gap_rect_bottomleft_y = gap_rect.bottomleft[1]
        gap_rect_topleft_x = gap_rect.topleft[0]
        gap_rect_topleft_y = gap_rect.topleft[1]
    
     #DRAW BOTTOM
        top_obstacle1.draw_rect_top_left(gap_rect_bottomleft_x, gap_rect_bottomleft_y)
    
    #DRAW TOP
        bottom_obstacle1.draw_rect_bottom_left(gap_rect_topleft_x, gap_rect_topleft_y)


def procedural_generate2(gap_x_pos, gap_y_pos, gap_height, scale):

        #gap rect
        gap_width = top_obstacle2.width
        gap_rect = pygame.rect.Rect((gap_x_pos, gap_y_pos), (gap_width, gap_height))
        gap_rect.midleft = (gap_x_pos, gap_y_pos)

            #GAP RECT POSITIONS
        gap_rect_bottomleft_x = gap_rect.bottomleft[0]
        gap_rect_bottomleft_y = gap_rect.bottomleft[1]
        gap_rect_topleft_x = gap_rect.topleft[0]
        gap_rect_topleft_y = gap_rect.topleft[1]
    
     #DRAW BOTTOM
        top_obstacle2.draw_rect_top_left(gap_rect_bottomleft_x, gap_rect_bottomleft_y)
    
    #DRAW TOP
        bottom_obstacle2.draw_rect_bottom_left(gap_rect_topleft_x, gap_rect_topleft_y)

    


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



#Player
big_chungus_pixel_file = "flappy chungus/Graphics/Sprites/pixelbigchungussprite.png"
big_chungus_pixel = pygame.image.load(big_chungus_pixel_file).convert_alpha()
big_chungus_pixel_width = big_chungus_pixel.get_width()
big_chungus_pixel_height = big_chungus_pixel.get_height()
scale = .1
big_chungus_pixel = pygame.transform.scale(big_chungus_pixel, ((big_chungus_pixel_width * scale), (big_chungus_pixel_height * scale)))
big_chungus_pixel_rect = big_chungus_pixel.get_rect()
big_chungus_pixel_rect.center = (50, SCREEN_HEIGHT/2)
PLAYER_GRAV = 0

#procedural generate 
obstacle_gap_lower = big_chungus_pixel_rect.height + 100
obstacle_gap_higher = big_chungus_pixel_rect.height + 600
top_limit  = 150
bottom_limit = SCREEN_HEIGHT - obstacle_gap_lower
gap_y_pos = SCREEN_HEIGHT/2
gap_x_pos1 = SCREEN_WIDTH/2
gap_x_pos2 = SCREEN_WIDTH + 200


#FONTS
hp_font = Font("flappy chungus/Graphics/Text/PermanentMarker-Regular.ttf", 50)

#CONDITIONS
game_active = False
if_play = False
game_over = False
menu_active = True

#BOOLS CONCERNING OBSTACLES
obst1_on_screen = False
obst2_on_screen = False
#RUN LOOP
run = True

#START TIME 
start_time = 0

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
                start_time = pygame.time.get_ticks()







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
        if obst2_on_screen == False and obst1_on_screen == False:
            top_obstacle1 = Sprite(uganda_knuckles_file, scale)
            bottom_obstacle1 = Sprite(uganda_knuckles_file, scale)
            gap_height1 = random.randint(obstacle_gap_lower, obstacle_gap_higher)
            gap_y_pos1 = random.randint(top_limit, bottom_limit)
            scale1 = random.randint(3,10)
            scale1 /= 10 

            #create obstacles
            top_obstacle1 = Sprite(uganda_knuckles_file, scale1)
            bottom_obstacle1 = Sprite(uganda_knuckles_file, scale1)
            #NO INF LOOPS
            obst1_on_screen = True

        #DRAW OBJ 1
        elif obst1_on_screen == False:
            gap_x_pos1 = SCREEN_WIDTH + 100
            gap_y_pos1 = random.randint(top_limit, bottom_limit)
            gap_height1 = random.randint(obstacle_gap_lower, obstacle_gap_higher)
            scale1 = random.randint(4,10)
            scale1 /= 10 

            #NO INF LOOPS
            obst1_on_screen = True

        if obst1_on_screen:
            procedural_generate1(gap_x_pos1, gap_y_pos1, gap_height1, scale1)
            gap_x_pos1 -= 4
            #DEATH 
            if top_obstacle1.rect.colliderect(big_chungus_pixel_rect) or bottom_obstacle1.rect.colliderect(big_chungus_pixel_rect):
                game_over = True


        #DRAW OBJECT 2
        if gap_x_pos1 < 300 and obst2_on_screen == False:
            #GENERATE RANDOM OBJECT
            gap_x_pos2 = SCREEN_WIDTH + 100
            gap_y_pos2 = random.randint(top_limit, bottom_limit)
            gap_height2 = random.randint(obstacle_gap_lower, obstacle_gap_higher)
            scale2 = random.randint(4,10)
            scale2 /= 10 

            #create obstacles
            top_obstacle2 = Sprite(uganda_knuckles_file, scale2)
            bottom_obstacle2 = Sprite(uganda_knuckles_file, scale2)
            
            #MAKE SURE NOT TO INFINITELY CREATE OBST
            obst2_on_screen = True

        if obst2_on_screen:
            procedural_generate2(gap_x_pos2, gap_y_pos2, gap_height2, scale2)
            gap_x_pos2 -= 4

            #DEATH
            if top_obstacle2.rect.colliderect(big_chungus_pixel_rect) or bottom_obstacle2.rect.colliderect(big_chungus_pixel_rect):
                game_over = True


        #KILL OBJS
        if gap_x_pos1 < -SCREEN_HEIGHT:
            obst1_on_screen = False
            check_score = False

        if gap_x_pos2 < -SCREEN_HEIGHT:
            obst2_on_screen = False
            check_score = False 

        #PLAYER
        PLAYER_GRAV += 1
        big_chungus_pixel_rect.y += PLAYER_GRAV
        if big_chungus_pixel_rect.bottom > SCREEN_HEIGHT:
            game_over = True
        elif big_chungus_pixel_rect.top < 50:
            big_chungus_pixel_rect.top = 50
        screen.blit(big_chungus_pixel, big_chungus_pixel_rect)

        #DRAW SCORE
        score_display()

    if game_over:
        screen.fill((60, 130, 200))
        PLAYER_GRAV = 0
        end_time = pygame.time.get_ticks()
        big_chungus_pixel_rect.center = (50, SCREEN_HEIGHT/2)
        play_again_button.draw(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        hp_font.messagedraw("Game Over...", SCREEN_WIDTH/2, 100)
        gap_x_pos1 = SCREEN_WIDTH/2
        gap_x_pos2 = SCREEN_WIDTH + 200

    #DISPLAY UPDATE
    pygame.display.update()

    #FRAMERATE
    clock.tick(60)

pygame.quit()

