import pygame
pygame.init()

display_width = 1100
display_height = 600
display = pygame.display.set_mode((display_width, display_height))

run = True

while run:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            run = False


    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    display.fill((255, 255, 255))

    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 296, display_height/2 + 54, 200, 100))  
    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 297, display_height/2 + 53, 200, 100))
    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 298, display_height/2 + 52, 200, 100))
    pygame.draw.rect(display, (0, 150, 0), (display_width/2 - 299, display_height/2 + 51, 200, 100))
    pygame.draw.rect(display, (0, 255, 0), (display_width/2 - 300, display_height/2 + 50, 200, 100))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('backward', 1, (0,0,0))
    display.blit(text, (display_width/2 - 295, display_height/2 + 70))

    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 96, display_height/2 + 54, 200, 100))  
    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 97, display_height/2 + 53, 200, 100))
    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 98, display_height/2 + 52, 200, 100))
    pygame.draw.rect(display, (150, 0, 0), (display_width/2 + 99, display_height/2 + 51, 200, 100))
    pygame.draw.rect(display, (255, 0, 0), (display_width/2 + 100, display_height/2 + 50, 200, 100))

    green_button_text = pygame.font.SysFont('arial', 48)
    text = green_button_text.render('forward', 1, (0,0,0))
    display.blit(text, (display_width/2 + 125, display_height/2 + 70))

    pygame.display.update()
