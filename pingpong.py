from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')

clock = time.Clock()
fps = 60
clock.tick(fps)

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        display.update()
    else:
        finish = False