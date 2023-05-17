from barbarian import Barbarian
from knight import Knight
import random



barb = Barbarian("Olaf")
knight = Knight("Arthur")

def barbauto():
    x = random.randint(0,1)
    if x==0:
        barb.attack(knight)
    else:
        barb.rage(knight)

def knightauto():
    x = random.randint(0,1)
    if x==0:
        knight.attack(barb)
    else:
        knight.heal()


player = input("choose your player : barb , knight : ")

while barb.health>0 and knight.health>0:


    if player=="barb":
        action = input("choose your action : 1)attack , 2)rage : ")
        if action == "1":
            barb.attack(knight)
            knightauto()
        if action == "2":
            barb.rage(knight)
            knightauto()

    if player=="knight":
        action = input("choose your action : 1)attack , 2)heal : ")
        if action == "1":
            knight.attack(barb)
            barbauto()
        if action == "2":
            knight.heal()
            barbauto()

print("GAME OVER")
if barb.health> knight.health:
    print("barb WIN")
else:
    print("knight WIN")