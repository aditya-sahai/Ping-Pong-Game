import pygame
import random
import time
import sys

pygame.init()

width = 800
height = 400

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

win = pygame.display.set_mode((width,height + 100))
ball_IMG = pygame.image.load('ball.png')
pygame.display.set_caption('Ping Pong Game')

scoreFont = pygame.font.Font('game_over.ttf',150)
button_font = pygame.font.Font('game_over.ttf',75)
head_font = pygame.font.Font('game_over.ttf',200)

class Player:
    def __init__(self,width,height,player_width,player_height,x,y_change):
        self.width = player_width
        self.height = player_height
        self.x = x
        self.y = int(height / 2 - (self.height / 2))
        self.y_change = y_change
        self.score = 0
        self.box = [self.x, self.y, self.width, self.height]

    def WallCheck(self,y_change):
        if self.y <= 0:
            self.y_change = y_change
        elif self.y + self.height >= height:
            self.y_change = -1 * y_change

class Ball:
    def __init__(self,width,height,size,x_change,y_change):
        self.size = size
        self.x = width / 2 - self.size / 2
        self.y = height / 2 - self.size / 2
        self.x_change = x_change
        self.y_change = y_change
        self.center_point = (int(self.x + self.size / 2), int(self.y + self.size / 2))

    def Collision(self,playerRed,playerBlue,width,height,ball_x_change,ball_y_change):
        if self.y <= 0 or self.y + self.size >= height:
            self.y_change *= -1
        if self.x <= 0:
            self.x_change *= -1
            playerRed.score += 1
            self.x = width / 2 - self.size / 2
            self.y = height / 2 - self.size / 2
            time.sleep(1)
        elif self.x + self.size >= width:
            self.x_change *= -1
            playerBlue.score += 1
            self.x = width / 2 - self.size / 2
            self.y = height / 2 - self.size / 2
            time.sleep(1)

        if circle.colliderect(blue_rect):
            self.x_change = ball_x_change
            ball_y_change = random.randint(5,11) * random.choice([-1,1])
            self.y_change = ball_y_change
        elif circle.colliderect(red_rect):
            self.x_change = -1 * ball_x_change
            ball_y_change = random.randint(5,11) * random.choice([-1,1])
            self.y_change = ball_y_change

def DrawGameWindow(win,playerRed,playerBlue,ball,ball_IMG,upper_rect,lower_rect,a):
    win.fill(white)
    bluescore = scoreFont.render(str(playerBlue.score),True,black)
    redscore = scoreFont.render(str(playerRed.score),True,black)
    pygame.draw.rect(win, green, (0,0,width,height))
    if a == 0:
        pass
        #pygame.draw.rect(win, red, upper_rect,2)
        #pygame.draw.rect(win, red, lower_rect,2)
    global red_rect
    global blue_rect
    global circle
    red_rect = pygame.draw.rect(win, red, playerRed.box)
    blue_rect = pygame.draw.rect(win, blue, playerBlue.box)
    circle = pygame.draw.circle(win, black, ball.center_point, int(ball.size / 2))
    win.blit(bluescore, (int((width / 2) / 2 - 75),height))
    win.blit(redscore, (int((width / 2) / 2 + (width / 2)),height))

def MessageOnScreen(win,width,height,message,y):
    text = scoreFont.render(str(message), True, black)
    text_rect = text.get_rect()
    text_rect.center = (int(width / 2), int(y))
    win.blit(text,text_rect)


def ScoreCheck(playerRed,playerBlue,width,height,win,ball,ball_IMG,upper_rect,lower_rect,a):
    if playerRed.score >= 2:
        ball.x = -100
        ball.y = -100
        DrawGameWindow(win,playerRed,playerBlue,ball,ball_IMG,upper_rect,lower_rect,a)
        MessageOnScreen(win,width,height,'Player Red Wins!', height / 2)
        pygame.display.update()
        time.sleep(2)
        return True
    elif playerBlue.score >= 2:
        ball.x = -100
        ball.y = -100
        DrawGameWindow(win,playerRed,playerBlue,ball,ball_IMG,upper_rect,lower_rect,a)
        MessageOnScreen(win,width,height,'Player Blue Wins!', height / 2)
        pygame.display.update()
        time.sleep(2)
        return True
    return False

def DisplayText(win, box1, box2, message1, message2):
    text1 = button_font.render(str(message1), True, black)
    text2 = button_font.render(str(message2), True, black)
    rect1 = text1.get_rect()
    rect2 = text2.get_rect()
    rect1.center = box1.center
    rect2.center = box2.center
    win.blit(text1, (rect1[0],rect1[1]))
    win.blit(text2, (rect2[0],rect1[1]))

def DrawIntroWindow(win,box1,box2,color1,color2):
    win.fill(white)
    MessageOnScreen(win,width,height, 'Ping Pong Game', 100)
    pygame.draw.rect(win, color1, box1)
    pygame.draw.rect(win, color2, box2)
    DisplayText(win,box1,box2,'Single Player', 'Multi Player')

def Intro(win):

    single_player_box = pygame.Rect(150, int(height / 2), 200, 100)
    multi_player_box = pygame.Rect(450, int(height / 2), 200, 100)

    game_over = False
    clock = pygame.time.Clock()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        mouse_pos = pygame.mouse.get_pos()

        if single_player_box.collidepoint(mouse_pos):
            DrawIntroWindow(win,single_player_box,multi_player_box,red,green)
            if pygame.mouse.get_pressed()[0] == 1:
                return 0
        elif multi_player_box.collidepoint(mouse_pos):
            DrawIntroWindow(win,single_player_box,multi_player_box,green,red)
            if 1 in pygame.mouse.get_pressed():
                return 1
        else:
            DrawIntroWindow(win,single_player_box,multi_player_box,green,green)

        pygame.display.update()
        clock.tick(30)

def GameLoop(a,win):
    player_width = 20
    player_height = 100
    player_y_change = 10
    Red = Player(width,height,player_width,player_height,width - player_width - 5,player_y_change)
    Blue = Player(width,height,player_width,player_height,5,player_y_change)

    ball_size = 32
    ball_x_change = 10
    ball_y_change = 0
    BOB = Ball(width,height,ball_size,ball_x_change,ball_y_change)

    game_over = False
    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Red.y_change = -1 * player_y_change
                elif event.key == pygame.K_DOWN:
                    Red.y_change = player_y_change
                if a == 1:
                    if event.key == pygame.K_w:
                        Blue.y_change = -1 * player_y_change
                    elif event.key == pygame.K_s:
                        Blue.y_change = player_y_change
        if a == 0:
            upper_rect = pygame.Rect(0,0,width, height - (height - Blue.y))
            lower_rect = pygame.Rect(0,Blue.y + Blue.height,width, height - (Blue.y + Blue.height))

            if upper_rect.collidepoint(BOB.center_point):
                Blue.y_change = -player_y_change
            if lower_rect.collidepoint(BOB.center_point):
                Blue.y_change = player_y_change
        DrawGameWindow(win,Red,Blue,BOB,ball_IMG,upper_rect,lower_rect,a)

        Red.WallCheck(player_y_change)
        Blue.WallCheck(player_y_change)
        BOB.Collision(Red,Blue,width,height,ball_x_change,ball_y_change)

        game_over = ScoreCheck(Red,Blue,width,height,win,BOB,ball_IMG,upper_rect,lower_rect,a)

        Red.y += Red.y_change
        Red.box[1] = Red.y
        Blue.y += Blue.y_change
        Blue.box[1] = Blue.y
        BOB.x += BOB.x_change
        BOB.y += BOB.y_change
        BOB.center_point = (int(BOB.x + BOB.size / 2), int(BOB.y + BOB.size / 2))

        pygame.display.update()
        clock.tick(30)


a = Intro(win)
if a != None:
    GameLoop(a,win)
