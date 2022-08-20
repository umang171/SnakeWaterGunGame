"""
snake>water
water>gun
gun>snake
"""
import random
li=["snake","water","gun"]
ys=0
cs=0
dr=0
# print(random.choice(li))
i=1
while (i<=10):
    you=input("s:snake/w:water/g:game:")
    if you=="s":
        you="snake"
    elif you=="w":
        you="water"
    elif you=="g":
        you="gun"
    else:
        print("invalid choice")
        break;
    com=random.choice(li)
    if you==com:
        dr+=1
        print(f"draw game com:{com} and you:{you}")
    elif you=="snake" and com=="water":
        ys+=1
        print(f"you won com:{com} and you:{you}")
    elif you=="snake" and com=="gun":
        cs+=1
        print(f"you lose com:{com} and you:{you}")
    elif you=="water" and com=="snake":
        cs += 1
        print(f"you lose com:{com} and you:{you}")
    elif you=="water" and com=="gun":
        ys += 1
        print(f"you won com:{com} and you:{you}")
    elif you=="gun" and com=="snake":
        ys += 1
        print(f"you won com:{com} and you:{you}")
    elif you=="gun" and com=="water":
        cs += 1
        print(f"you lose com:{com} and you:{you}")
    print(f"game left {10-i} times")
    i+=1
if(ys>cs):
    print("congretulations you won the game")
elif(cs>ys):
    print("sorry you lose game")
else:
    print("Draw ho gaya")
print(f"scorecard:\nYour score:{ys}\nComputer:{cs}\nDraw:{dr}")