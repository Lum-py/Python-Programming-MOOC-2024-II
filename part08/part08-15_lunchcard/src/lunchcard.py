# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
        self.lunch = 2.60
        self.special = 4.60
    
    def deposit_money(self, deposit: float):
        if deposit < 0:
            raise ValueError ("You cannot deposit an amount of money less than zero")
        self.balance += deposit        


    def eat_lunch(self):
        if self.balance >= self.lunch:
            self.balance -= self.lunch

    def eat_special(self):
        if self.balance >= self.special:
            self.balance -= self.special

    def __str__(self) -> str:
        return f"The balance is {float(self.balance):.1f} euros"
        
        
peters_card = LunchCard(20)
graces_card = LunchCard(30)
peters_card.eat_special()
graces_card.eat_lunch()
print("Peter:", peters_card)
print("Grace:", graces_card)
peters_card.deposit_money(20)
graces_card.eat_special()
print("Peter:", peters_card)
print("Grace:", graces_card)
peters_card.eat_lunch()
peters_card.eat_lunch()
graces_card.deposit_money(50)
print("Peter:", peters_card)
print("Grace:", graces_card)