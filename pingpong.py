from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_img,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img),(26,140))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def drop(self):
        window.blit(self.image,(self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        global num_fire
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 1050
win_height = 1000

window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')

background = transform.scale(image.load('white_bkg.png'),(win_width,win_height))

clock = time.Clock()
fps = 60
clock.tick(fps)

game = True
finish = False
pl1 = Player('racket.png',20,200,5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        pl1.update()
        pl1.drop()
        display.update()
    else:
        finish = False