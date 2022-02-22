#슈팅게임 준비
import pygame as p
import random as r 

p.init()
w =(255,255,255)








size = (600,900)
sc = p.display.set_mode(size)
p.display.set_caption("슈팅게임")
playing = True

p_image = p.image.load("pp.png")
p_rect = p_image.get_rect(left=250,top = 750)
x = 0
y = 0

bg = p.image.load("space.png")

b_image = p.image.load("bul.png")
b_list = []

e_image = p.image.load("enemy.png")
e_list = []
for x in range(10):
    e_rect = e_image.get_rect(left = r.randint(0,520),top = 0)
    e_list.append(e_rect)
    
score = 0
font = p.font.SysFont('malgungothic',30)
lose = 0
font2 = p.font.SysFont("malgungothic",50)
ex = p.image.load("ex.png")


            

while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                y =-5
            if event.key == p.K_DOWN:
                y = 5
            if event.key == p.K_LEFT:
                x =-5
            if event.key == p.K_RIGHT:
                x = 5
            if event.key == p.K_SPACE:
                b_rect = b_image.get_rect(left=p_rect.left+45, top=p_rect.top)
                b_list.append(b_rect)
        if event.type == p.KEYUP:
            if event.key == p.K_UP:
                y = 0
            if event.key == p.K_DOWN:
                y = 0
            if event.key == p.K_LEFT:
                x = 0
            if event.key == p.K_RIGHT:
                x = 0
                
    p_rect.left += x     # += --> p_rect.left = p_rectt.left + x
    p_rect.top += y
   
    
    sc.fill(w)
    sc.blit(bg,(0,0))
    for b_rect in b_list:
        sc.blit(b_image,b_rect)
    for b_rect in b_list:
        b_rect.top -= 5
        if b_rect.top <= 10:
            b_list.remove(b_rect)
    

        
    sc.blit(p_image,p_rect) #비행기 업로드

    for e_rect in e_list:
        sc.blit(e_image,e_rect)
    for e_rect in e_list:
        e_rect.top += 4
        if e_rect.top >= 850:
            e_list.remove(e_rect)
            lose += 1
            e_rect = e_image.get_rect(left = r.randint(0,520),top = 0)
            e_list.append(e_rect)
            
    for e_rect in e_list:
        for b_rect in b_list:
            if b_rect.colliderect(e_rect):
                sc.blit(ex,e_rect)
                b_list.remove(b_rect)
                e_list.remove(e_rect)
                score += 1
                e_rect = e_image.get_rect(left = r.randint(0,520),top = 0)
                e_list.append(e_rect)

    text = font.render("점수: {}".format(score),True,(255,255,0))
    text2 = font.render("놓친 적기 개수: {}".format(lose),True,(255,255,0))
    text3 = font2.render("Game over",True,(255,0,0))
    sc.blit(text,(50,50))
    sc.blit(text2,(350,50))
    
    
    
    if lose>=15:
        sc.blit(text3,(170,350))
        playing = False
        

    p.display.flip()

    
