#벽돌깨기 게임
import pygame as p

p.init()
w =(255,255,255)
size = (600,800)
sc = p.display.set_mode(size)
p.display.set_caption("벽돌깨기")
playing = True


pan = p.image.load("phan.png")
p_rect = pan.get_rect(left = 245, top = 740)
px = 0
bg = p.image.load("bg.png")

bl = p.image.load("ball.png")
bl_rect = bl.get_rect(left = 270, top = 370)
bx=10
by=10

font = p.font.SysFont("malgungothic",50)

blo = p.image.load("blo2.png")
blo_list = []

score = 0
f1 = p.font.SysFont("malgungothic",20)


for x in range(10):
    for y in range(5):
        blo_rect = blo.get_rect(left = 60*x, top = 50*y)
        blo_list.append(blo_rect)
    
while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                px = -10
            if event.key == p.K_RIGHT:
                px = 10
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                px = 0
            if event.key == p.K_RIGHT:
                px = 0
                
    p_rect.left += px

    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(pan,p_rect)
    
    if p_rect.left >= 500:
        p_rect.left = 500
    if p_rect.left <= 0:
        p_rect.left = 0
    sc.blit(bl,bl_rect)

    bl_rect.top += by
    bl_rect.left += bx
    if bl_rect.top >=770:
        by = -by
    if bl_rect.top <=10:
        by = -by
    if bl_rect.left >=550:
        bx = -bx
    if bl_rect.left <=10:
        bx = -bx
        
    text = font.render("Game Over",True,(0,255,0))
    if bl_rect.top >=770:
        by = -by
        sc.blit(text,(180,370))
        playing = False

    if p_rect.colliderect(bl_rect):
        by = -2

    for blo_rect in blo_list:
        sc.blit(blo,blo_rect)

    for blo_rect in blo_list:
        if blo_rect.colliderect(bl_rect):
            blo_list.remove(blo_rect)
            by = 2
            score = score + 1

    text1 = f1.render("점수 : {}".format(score),True,(255,255,0))
    sc.blit(text1,(50,750))

        
    text2 = font.render("Clear",True,(255,0,255))
    if len(blo_list) <= 0:
        sc.blit(text2,(220,370))
        playing = False
        
        
    p.display.flip()
