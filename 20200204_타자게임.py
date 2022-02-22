#타자게임
import random
import time

animal = ["dog", "cat", "fox", "panda", "mouse", "snake", "frog", "tiger"]

n = 1

print ("[타자 게임] 준비 되면 엔터!!!")
input()
start = time.time()

q = random.choice(animal)

while n <= 5:
    print("문제", n)
    print(q)
    x = input()

    if q == x :
        print("pass")
        n = n + 1
        q = random.choice(animal)
    else :
        print("fail try again")

end = time.time()
et = end - start
et2 = format(et, ".2f")

print ("타자시간 : ", et2,"초")
    






