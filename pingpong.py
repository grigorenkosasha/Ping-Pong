from pygame import *
import random

pause = True

class GameSprite(sprite.Sprite):
    size = (26,140)
    def __init__(self,player_img,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img),self.size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def drop(self):
        window.blit(self.image,(self.rect.x, self.rect.y)) 

class Player(GameSprite):
    Key_up = K_w
    Key_down = K_s
    loose = False
    def update(self):
        global pause 
        keys = key.get_pressed()
        if keys[self.Key_up] and self.rect.y > 5:
            self.rect.y -= self.speed
            pause = False
            self.loose = False
        if keys[self.Key_down] and self.rect.y < win_height - 145:
            self.rect.y += self.speed
            pause = False
            self.loose = False

class Player2(Player):
    Key_up = K_UP
    Key_down = K_DOWN

class Enemy(GameSprite):
    size = (28,28)
    speed_x = 1
    speed_y = 1
    def update(self):
        global pause
        if pause:
            return 

        self.rect.y = self.rect.y + self.speed_y * self.speed
        self.rect.x = self.rect.x + self.speed_x * self.speed

        # if self.rect.x >= win_width-28:
        #     self.speed_x = -1

        if self.rect.y >= win_height-28:
            self.speed_y *= -1

        if self.rect.y <= 0:
            self.speed_y = 1

        # if self.rect.x <= 0:
        #     self.speed_x = 1

font.init()
font1 = font.SysFont('Arial', 36) 
msg_rlose = font1.render("ПРАВЫЙ ПРОИГРАЛ!", True, (255,0,0))
msg_llose = font1.render("ЛЕВЫЙ ПРОИГРАЛ!", True, (0,255,0))

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')

background = transform.scale(image.load('white_bkg.png'),(win_width,win_height))

clock = time.Clock()
fps = 60
clock.tick(fps)

game = True
finish = False
pl1 = Player('racket.png',20,150,5)
pl2 = Player2('racket.png',650,150,5)
ball = Enemy('bal.png',350,250,2)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if sprite.collide_rect(ball,pl2) or sprite.collide_rect(ball,pl1):
        ball.speed_x *= -1

    if ball.rect.x >= win_width-28:
        ball.rect.x = 350
        ball.rect.y = 250
        pause = True
        pl2.loose = True

    if ball.rect.x <= 0:
        ball.rect.x = 350
        ball.rect.y = 250
        pause = True
        pl1.loose = True
            

    if finish != True:
        window.blit(background, (0,0))

        if pl2.loose:
            window.blit(msg_rlose,(250,200))

        if pl1.loose:
            window.blit(msg_llose,(250,200))

        pl1.update()
        pl1.drop()
        pl2.update()
        pl2.drop()
        ball.update()
        ball.drop()
        display.update()
    else:
        finish = False