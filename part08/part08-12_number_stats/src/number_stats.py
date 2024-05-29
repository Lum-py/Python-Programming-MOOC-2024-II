# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total = 0

    def add_number(self, number:int):
        self.numbers += 1        
        self.total += number                

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        return self.total
    
    def average(self):
        if self.numbers > 0:
            return self.total / self.numbers
        else: 
            return 0

stats = NumberStats()
even = NumberStats()
odd = NumberStats()

print("Please type in integer numbers:")     
while True:
    user_input = int(input(""))
    if user_input < 0:
        break
    stats.add_number(user_input)
    if user_input % 2 == 0:
        even.add_number(user_input)
    else:
        odd.add_number(user_input)


print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:", even.get_sum())
print("Sum of odd numbers:", odd.get_sum())


