import pygame as p
import random as r

p.init()

size = (800,400)   #가로, 세로

sc = p.display.set_mode(size)

p.display.set_caption("키보드 조작")

w = (255,255,255)
b = (0,0,0)
pl = p.image.load("plane2.png")
pl_rect = pl.get_rect(left = 10 , top = 0)

bg = p.image.load("bg3.png")
bg_rect = bg.get_rect(left= 0, top = 0)
          
bg1 = bg.copy()
bg1_rect = bg1.get_rect(left = 800, top = 0 )
en = p.image.load("en22.png")
en_rect = en.get_rect(left = 700, top = 200)

font = p.font.SysFont('malgungothic', 20)
font1 = p.font.SysFont('malgungothic', 50)

bo = p.image.load("exp.png")


x = 0
y = 0 
y_1 = 0
bg_x = 0
bg1_x = 800
en_x = 700
en_y = 0
score = 0

playing = True

while playing:

    for event in p.event.get():
        if event.type ==p.QUIT:
            playing = False
            p.quit()
            quit
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                print("위 방향키를 눌렀습니다")
                y = -5
            if event.key == p.K_DOWN:
                print("아래 방향키를 눌렀습니다")
                y = 5
                 
        if event.type == p.KEYUP:
            if event.key == p.K_UP or event.key == p.K_DOWN:
                y = 0
            
    pl_rect.top += y
    
    sc.fill(w)
    sc.blit(bg,bg_rect)
    sc.blit(bg1,bg1_rect)
    bg_rect.left -= 2
    bg1_rect.left -= 2
    if bg_rect.left <= -800:
        bg_rect.left = 800
    if bg1_rect.left <= -800:
        bg1_rect.left = 800
        
    
    sc.blit(pl,pl_rect)
    if pl_rect.top >= 325:
        y = 0

    if pl_rect.top <= -14:
        y = 0
        
    sc.blit(en,en_rect)
    en_rect.left -= 12
    if en_rect.left <= 0:
        en_rect.left  = 800
        en_rect.top  = r.randint(0,300)
        score += 1

    text = font.render('점수:{}'.format(score),True,(255,255,0))
    text1 = font1.render('Game over',True,(255,0,0))
    sc.blit(text,(400,0))

    if pl_rect.colliderect(en_rect):
        sc.blit(bo,pl_rect)
        sc.blit(text1,(300,150))
        playing = False
        

        
    p.display.flip()


        
    
