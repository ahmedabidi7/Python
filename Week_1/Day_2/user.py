class user:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("first_name : "+self.first_name)
        print("last_name : "+self.last_name)
        print("email : "+self.email)
        print("age : "+str(self.age))
        print("is_rewards_member : "+str(self.is_rewards_member))
        print("gold_card_points : "+str(self.gold_card_points))

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        self.gold_card_points -= amount

        return self
    
user1 = user("hammadi","ben mahmoud","hamadi@gmail.com",33)
user1.display_info()

user1.enroll()

user2 = user("foulen","ben foulen","foulen@gmail.com",27)
user3 = user("aziz","barreh","aziz@gmail.com",16)

user1.spend_points(50)

user2.enroll()

user2.spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()

