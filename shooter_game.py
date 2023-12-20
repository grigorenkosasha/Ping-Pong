from pygame import *
import random
from time import time as timer

num_fire = 0
last_time = timer()
class GameSprite(sprite.Sprite):
    def __init__(self,player_img,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img),(75,75))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def drop(self):
        win.blit(self.image,(self.rect.x, self.rect.y)) 

class Player(GameSprite):
    def update(self):
        global num_fire
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            if num_fire <= 5:
                self.fire()

    def fire(self):
        global last_time
        global bullets
        global num_fire
        global rel_time
        bullet = Bullet("bullet.png",self.rect.centerx, self.rect.top,15) 
        bullets.add(bullet)
        num_fire = num_fire + 1
        if num_fire == 5:
            last_time = timer()
lost = 0
class Enemy(GameSprite):
    def __init__(self,player_speed, player_img = 'ufo.png'):
        super().__init__(player_img,random.randint(0,win_width - 65),0,player_speed)
    def update(self):
        self.rect.y += self.speed
        global lost

        if self.rect.y >= 470:
            self.rect.y = 0
            self.rect.x = random.randint(0, win_width-65)
            self.speed = random.randint(2,4)
            self.add_lost()

    def add_lost(self):
        global lost
        lost = lost +1

class Asteroid(Enemy):
    def __init__(self, player_speed, player_img = 'asteroid.png'):
        super().__init__(player_speed, player_img)
    def add_lost(self):
        pass 

class Bullet(GameSprite):
    def __init__(self, player_img,player_x,player_y,player_speed=10):
        super().__init__(player_img,player_x,player_y,player_speed)
        self.image = transform.scale(image.load(player_img),(20,30))
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
   
font.init()
font1 = font.SysFont('Arial', 36) 
msg_win = font1.render("YOU WIN", True, (255,215,0))
msg_lose = font1.render("YOU LOSE", True, (255,215,0))





bullets = sprite.Group()
#bullets.add(Bullet('bullet.png',100,400,5))
win_width = 700
win_height = 500

win = display.set_mode((win_width,win_height))
display.set_caption('Shuter')

background = transform.scale(image.load('galaxy.jpg'),(win_width,win_height))

clock = time.Clock()
fps = 60
clock.tick(fps)
 
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0)
mixer.music.play()
#fire = mixer.Sound('fire.ogg')

game = True
finish = False
rocket = Player('rocket.png',300,400,5) 
# ufo1 = Enemy('ufo.png',random.randint(0,win_width - 65),0,5)
# ufo2 = Enemy('ufo.png',random.randint(0,win_width - 65),0,5)
point = 0

monsters = sprite.Group()
for i in range(0,5):
    monsters.add(Enemy(random.randint(1,2)))

asteroids = sprite.Group()

for i in range(0,3):
    asteroids.add(Asteroid(random.randint(1,3)))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        if timer() - last_time > 3 and num_fire >= 5:
            num_fire = 0
        win.blit( background, (0,0))
        rocket.update()    
        rocket.drop()
        # ufo1.update()    
        # ufo1.drop()
        # ufo2.update()    
        # ufo2.drop()
        asteroids.update()
        asteroids.draw(win)
        monsters.update()
        monsters.draw(win)
        sprites_list = sprite.groupcollide(
            monsters, bullets, True, True
        )
        if len(sprites_list):
            monsters.add(Enemy(random.randint(1,2)))
            point = point +1
        if lost >= 10:
            # or sprite.spritecollide(rocket, monsters, False)\
            #or sprite.spritecollide(rocket, asteroids, False):
            win.blit(msg_lose, (300,200))
            finish = True
        if point == 10:
            win.blit(msg_win,(100, 100))
            finish = True
        if num_fire >= 5 and timer() - last_time <= 3:
            win.blit(text_reload, (270,450))
        bullets.update()
        bullets.draw(win)
        text_reload = font1.render("Wait reload...", 1,(255,255,255))
        text_lose = font1.render('Пропущено:' + str(lost),1,(255,255,255))
        win.blit(text_lose, (0,25))
        text_kill = font1.render('Счёт:' + str(point), 1,(255,255,255))
        win.blit(text_kill, (0,5))
        display.update()
        #clock.tick(fps)
    else:
        lost = 0
        point = 0
        finish = False
        time.delay(3000)
    time.delay(10)