from pygame import *
import random

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
    def update(self):
        keys = key.get_pressed()
        if keys[self.Key_up] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[self.Key_down] and self.rect.y < win_height - 145:
            self.rect.y += self.speed

class Player2(Player):
    Key_up = K_UP
    Key_down = K_DOWN

class Enemy(GameSprite):
    size = (28,28)
    def __init__(self,player_speed, player_img = 'bal.png'):
        super().__init__(player_img,random.randint(0,win_width - 65),0,player_speed)
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 470:
            self.rect.y = 0
            self.rect.x = random.randint(0, win_width-65)
            self.speed = random.randint(2,2)

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
ball = Enemy(10)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        pl1.update()
        pl1.drop()
        pl2.update()
        pl2.drop()
        ball.update()
        ball.drop()
        display.update()
    else:
        finish = False