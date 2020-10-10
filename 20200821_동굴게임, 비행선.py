import pygame as p
import copy
import random as r

p.init()
w =(255,255,255)

cyan = (102,255,255)
black = (0,0,0)

size = (800,600)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True

plane = p.image.load("pl.png")
p_rect = plane.get_rect(left =0 ,top =300)
p_y = 15

clock = p.time.Clock()

caves = []
for x in range(80):
    cave = p.Rect(10*x,100,10,400)
    caves.append(cave)
    
slope = 2

boom = p.image.load("ex.png")
game_over = False

font = p.font.SysFont("malgungothic",20)
score = 0


b = p.image.load("100.png")
while playing:
    clock.tick(20)
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_SPACE:
                p_y = -15
        if event.type == p.KEYUP:
            if event.key == p.K_SPACE:
                p_y = 15  

    sc.fill(cyan)
    for cave in caves:
        p.draw.rect(sc,black,cave)
        
    for cave in caves:
        cave.left = cave.left - 10
    del caves[0]

    new_cave = copy.deepcopy(caves[-1])
    new_cave.left = new_cave.left + 10
    new_cave.top = new_cave.top + slope
    caves.append(new_cave)
    score += 1

    t_cave = copy.deepcopy(caves[-1])
    t_cave.top = t_cave.top + slope
    if t_cave.top <= 0 or t_cave.bottom >= 600:#동굴에 화면 위,아래에 닿으면
        slope = r.randint(2,6) * (-1 if slope > 0 else 1)
        new_cave.height = new_cave.height + -20
        

    if p_rect.top <caves[0].top or p_rect.bottom > caves[0].bottom:
        game_over = True
    
    if game_over:
        b_rect = boom.get_rect(left = p_rect.left, top = p_rect.top-10)
        sc.blit(boom,b_rect)
        playing = False
    else:
        sc.blit(plane,p_rect)

    text = font.render("점수 : {}".format(score),True,(255,0,0))
    sc.blit(text,(50,50))
            
    p_rect.top += p_y
    p.display.flip()
