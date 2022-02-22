#두더지 게임
import pygame as p
import random as r
import time as t

p.init()
w =(255,255,255)
size = (800,400)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True

do = p.image.load("dodo.png")
do_list = []
for x in range(10):
    do_rect = do.get_rect(left=r.randint(0,700),top=r.randint(0,300))
    do_list.append(do_rect)

font = p.font.SysFont('malgungothic',20)
score = 0
#남은시간
t1 =  int(t.time()) #멈춘시간


p.mixer.init()#초기화
hit = p.mixer.Sound("www.wav")


while playing:
    t2 = int(t.time()) #흐르는 시간
    timer = 60 - (t2 - t1)
    print (timer)

    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type == p.MOUSEBUTTONDOWN:
           for do_rect in do_list:
               if do_rect.collidepoint(event.pos[0],event.pos[1]):
                   do_list.remove(do_rect)
                   do_rect = do.get_rect(left=r.randint(0,700),top=r.randint(0,300))
                   do_list.append(do_rect)
                   score +=1 #score = score + 1
                   hit.play() 
           
    sc.fill(w)
    for do_rect in do_list:
        sc .blit(do,do_rect)

    if timer == 0:
        playing = False
        
    text = font.render("점수:{}".format(score),True,(0,0,0))
    sc.blit(text,(415,0))
    text1 = font.render("남은시간: {}".format(timer),True,(0,0,0))
    sc.blit(text1,(675,0))
    
     
    p.display.flip()
