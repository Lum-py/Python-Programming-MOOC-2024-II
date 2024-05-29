# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.lunches = 0
        self.specials = 0
        self.lunch = 2.50
        self.special = 4.30

    def eat_lunch(self, payment: float):
        if not payment >= self.lunch:
            return payment
        self.lunches += 1
        self.funds += self.lunch
        return payment - self.lunch

    def eat_special(self, payment: float):
        if not payment >= self.special:
            return payment
        self.specials += 1
        self.funds += self.special
        return payment - self.special

    def eat_lunch_lunchcard(self, card: LunchCard):
        if not card.subtract_from_balance(self.lunch):
            return False
        self.lunches += 1
        return True
        

    def eat_special_lunchcard(self, card: LunchCard):
        if not card.subtract_from_balance(self.special):
            return False
        self.specials += 1
        return True


    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount

if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)