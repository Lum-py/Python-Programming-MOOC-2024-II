# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"
    
    def __date(self):
        return f"{self.year}{self.month:02d}{self.day:02d}"
    
    def __eq__(self, other: "SimpleDate"):
        return self.__date() == other.__date()

    def __ne__(self, other: "SimpleDate"):
        return self.__date() != other.__date()

    def __gt__(self, other: "SimpleDate"):
        return self.__date() > other.__date()

    def __lt__(self, other: "SimpleDate"):
        return self.__date() < other.__date()
    
    def __total_days(self):
        return (self.year * 360) + (self.month * 30) + self.day
    
    def __add__(self, days: int):
        total_days = self.__total_days() + days
        year = total_days // 360
        remainder = total_days % 360
        month = remainder // 30
        day = remainder % 30        
        return SimpleDate(day, month, year)
    
    def __sub__(self, other: "SimpleDate"):
        return abs(self.__total_days() - other.__total_days())
        

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)