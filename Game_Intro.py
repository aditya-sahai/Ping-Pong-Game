import pygame

pygame.init()

width = 800
height = 500
win = pygame.display.set_mode((width,height))
button_font = pygame.font.Font('game_over.ttf',75)
head_font = pygame.font.Font('game_over.ttf',200)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def DisplayText(win, box1, box2, message1, message2):
    text1 = button_font.render(str(message1), True, black)
    text2 = button_font.render(str(message2), True, black)
    rect1 = text1.get_rect()
    rect2 = text2.get_rect()
    rect1.center = box1.center
    rect2.center = box2.center
    win.blit(text1, (rect1[0],rect1[1]))
    win.blit(text2, (rect2[0],rect1[1]))

def WriteHeading(win,message):
    heading = head_font.render(str(message), True, black)
    heading_rect = heading.get_rect()
    heading_rect.center = (int(width / 2), 100)
    win.blit(heading, (heading_rect[0],heading_rect[1]))

def DrawGameWindow(win,box1,box2,color1,color2):
    win.fill(white)
    WriteHeading(win, 'Ping Pong Game')
    pygame.draw.rect(win, color1, box1)
    pygame.draw.rect(win, color2, box2)
    DisplayText(win,box1,box2,'Single Player', 'Multi Player')

def Intro():

    single_player_box = pygame.Rect(150, int(height / 2), 200, 100)
    multi_player_box = pygame.Rect(450, int(height / 2), 200, 100)

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        mouse_pos = pygame.mouse.get_pos()

        if single_player_box.collidepoint(mouse_pos):
            DrawGameWindow(win,single_player_box,multi_player_box,red,green)
            if pygame.mouse.get_pressed()[0] == 1:
                print(1)
        elif multi_player_box.collidepoint(mouse_pos):
            DrawGameWindow(win,single_player_box,multi_player_box,green,red)
            if 1 in pygame.mouse.get_pressed():
                print('Entered Game')
        else:
            DrawGameWindow(win,single_player_box,multi_player_box,green,green)

        pygame.display.update()

    pygame.quit()

Intro()
