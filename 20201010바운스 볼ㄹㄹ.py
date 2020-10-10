import pygame as p

p.init()
w =(255,255,255)
size = (1000,600)
sc = p.display.set_mode(size)
p.display.set_caption("bounce_ball")
playing = True

ball = p.image.load("kong.png")
b_rect = ball.get_rect(left=470, top=270)
b_x = 0
b_y = 0 

clock = p.time.Clock()


b = p.image.load("100.png")
while playing:
    clock.tick(50)
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()

    sc.fill(w)
    sc.blit(ball,(b_rect))

    b_rect.top += b_y
    b_y = b_y + 1
    if b_rect.top >= 580:
        b_y = -20
    p.display.flip()
