class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet
    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()

class Pet:
    def __init__(self,name,type,tricks):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.energy=100
        self.health=100
    def sleep(self):
        self.energy+=25
    def eat(self):
        self.energy+=5
        self.health+=10
    def play(self):
        self.health+=5
    def noise(self):
        if self.type=="dog":
            print("ouf ouf")
        if self.type=="cat":
            print("miaw miaw")
        else:
            print("moooo")

ninja=Ninja("ali","ninja","playful","cat food",Pet("gatous","cat","jumping"))
ninja.feed()
ninja.walk()
ninja.bathe()
