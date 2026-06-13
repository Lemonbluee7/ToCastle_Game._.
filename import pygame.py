import pygame 
import gif_pygame



pygame.init()

screen = pygame.display.set_mode((800,600))
#Window

pygame.display.set_caption("GetToCastle")

#screens
laoding_screen = pygame.image.load("loadscreen.png").convert()
laoding_screen = pygame.transform.scale(laoding_screen,(800,600))

black_trans_screen = pygame.image.load("blackinfoscreen.png").convert()
black_trans_screen = pygame.transform.scale(black_trans_screen,(800,600))

levels = pygame.image.load("levelscreen.png").convert()
levels = pygame.transform.scale(levels,(800,600))

#gifs
tocastlelogo = gif_pygame.load("tocastle_logo.gif") #Logo

green_start_button_gif = gif_pygame.load("greenstartbutton.gif") #Green Button
green_start_button_gif_rec = green_start_button_gif.get_rect(topleft=(350,270))
green_start_button_gif_rec.size = (90,40)


red_exit_button_gif = gif_pygame.load("exitbutton.gif") #Red Button
red_exit_button_gif_rect = red_exit_button_gif.get_rect(topleft=(370,330))
red_exit_button_gif_rect.size = (50, 30)

#images
info_circle = pygame.image.load("info_circle.png").convert_alpha() #info Button
info_circle_rect = info_circle.get_rect(topleft=(383,370))
info_circle_rect.size = (27,29)

info_text = pygame.image.load("infotext.png").convert_alpha() #Credits

return_button = pygame.image.load("returnbutton.png").convert_alpha() #Return Button
return_button_rect = return_button.get_rect(topleft=(35,35))
return_button_rect.size = (50,50)

#Movements
info_text_y = 0
        

running = True
current_screen = None
menu = True
show_info = False
levels_screen = False

while running:
    mouse_pos = pygame.mouse.get_pos()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit() 
        
        if (event.type == pygame.MOUSEBUTTONDOWN
            and current_screen == "menu"):
             if red_exit_button_gif_rect.collidepoint(mouse_pos):
                  running = False
        
        if (event.type == pygame.MOUSEBUTTONDOWN
            and current_screen == "menu"):
            if green_start_button_gif_rec.collidepoint(mouse_pos):
                levels_screen = True
                menu = False

        if (event.type == pygame.MOUSEBUTTONDOWN
            and current_screen == "menu"):
            if info_circle_rect.collidepoint(mouse_pos):
                show_info = True
                menu = False
        
        if (event.type == pygame.MOUSEBUTTONDOWN 
            and return_button_rect.collidepoint(mouse_pos)):
            if current_screen == "info screen":
                show_info = False
                menu = True

            elif current_screen == "levels screen":
                levels_screen = False
                menu = True

             
    if menu:
        current_screen = "menu"

        screen.blit(laoding_screen,(0,0))
        screen.blit(tocastlelogo.blit_ready(),(250,10))
        screen.blit(green_start_button_gif.blit_ready().convert_alpha(), (350, 250))
        screen.blit(red_exit_button_gif.blit_ready().convert_alpha(),(350,300))
        screen.blit(info_circle,(383,370))
 
    
    if show_info:
        current_screen = "info screen"
        
        screen.blit(black_trans_screen,(0,0))
        screen.blit(return_button,(20,20))

        info_text_y -=0.5
        if(info_text_y== -805):
            info_text_y = 800
        screen.blit(info_text,(95,info_text_y))
        
    if levels_screen:
        current_screen = "levels screen"
        
        screen.blit(levels,(0,0))
        screen.blit(return_button,(20,20))

        
        

    # pygame.draw.rect(screen, (255,0,0), return_button_rect, 2)

    
    
    pygame.display.update()
