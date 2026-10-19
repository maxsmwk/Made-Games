import pygame 

def timer():
    current_time = pygame.time.get_ticks() - start_time
    sec = current_time // 1000
    minutes = current_time // 60000
    hours = current_time // 360000
    if sec > 60:
        new_time_sec = pygame.time.get_ticks()
        current_time -= new_time_sec
        seconds = current_time // 1000
    if minutes > 60:
        new_time_min = pygame.time.get_ticks()
        current_time -= new_time_min
        seconds = current_time // 60000
    string_timer = str(hours) + ":"+ str(minutes) + ":" + str(sec)
    timer_surf = test_font.render(string_timer, False, "Red")
    timer_rect = timer_surf.get_rect(center = (600, 200))
    screen.blit(timer_surf, timer_rect)


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("test game")

clock = pygame.time.Clock()


example_button = "Game 1/graphics/buttonsprites/exbutton.png"

class Button:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def draw(self, x, y):
        screen.blit(self.image, (x,y))




game_active = True
start_time = 0

test_font = pygame.font.Font("Game 1/graphics/textfonts/HARRYP__.TTF", 50)
text_surface = test_font.render("Hello World", False, "Red")
text_surface2 = test_font.render("Game Over", False, "Red")
text_rect2 = text_surface2.get_rect(center = (400, 200))

text_rect = text_surface.get_rect(center = (400, 50))
wooden_floor = pygame.image.load("Game 1/graphics/scenes/woodenfloor.png")
snail_surface = pygame.image.load("Game 1/graphics/charactersprites/snail/snail1.png")
snail_rect = snail_surface.get_rect(center = (700,300))
snail_x_pos = 600
player_surf = pygame.image.load("Game 1/graphics/charactersprites/lilguy.png").convert_alpha()

player_x_pos = 300
player_y_pos = 300
player_rect = player_surf.get_rect(center = (player_x_pos,player_y_pos))
player_gravity = 0

example_button = Button(example_button)
run = True


while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                player_gravity = -10

        if game_active == False:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 700
                start_time = pygame.time.get_ticks()
            

    keys = pygame.key.get_pressed()
    if game_active:
        if keys[pygame.K_w]:
            player_rect.y -= 4
        if keys[pygame.K_a]:
            player_rect.x -= 4
        if keys[pygame.K_s]:
            player_rect.y += 4
        if keys[pygame.K_d]:
            player_rect.x += 4
        if keys[pygame.K_SPACE]:
            if player_rect.bottom >= 300:
                player_gravity = -20

    if game_active:
        screen.fill("Black")
        timer()
        example_button.draw(200, 50)
        screen.blit(wooden_floor, (300, 300))
        pygame.draw.rect(screen, "Pink", text_rect)
        pygame.draw.rect(screen, "Green", text_rect, 3)
        screen.blit(text_surface, text_rect)
        snail_rect.x -= 1
        if snail_rect.left >= 815: 
            snail_rect.center = (700, 300)
        elif snail_rect.right <= 0:
            snail_rect.center = (700, 300)
        screen.blit(snail_surface, snail_rect)
        
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        
        if player_rect.colliderect(snail_rect):
            print("death")
            game_active = False

    else:
        screen.fill("White")
        screen.blit(text_surface2, text_rect2)


        
        mouse_pos = pygame.mouse.get_pos()
            #if example_button.collidepoint((mouse_pos)):
                #print(pygame.mouse.get_pressed())
    pygame.display.update()
    clock.tick(60)

pygame.quit()