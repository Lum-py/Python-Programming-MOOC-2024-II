# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__content = []
        self.__total = 0
        

    def add_item(self, item: Item):
        if self.__total + item.weight() <= self.__max_weight:
            self.__content.append(item)
            self.__total += item.weight()

    def print_items(self):
        if self.__content:
            [print(item) for item in self.__content]

    def weight(self):
        return self.__total
    
    def heaviest_item(self):
        heaviest = None
        weight = 0
        for item in self.__content:
            if item.weight() > weight:
                weight = item.weight()
                heaviest = item
        return heaviest

    def __str__(self) -> str: 
        plural = "item" if len(self.__content) == 1 else "items"
        return f"{len(self.__content)} {plural} ({self.__total} kg)"
    
class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.__content = []
        self.__total = 0

    def add_suitcase(self, suitcase: Suitcase):
        if self.__total + suitcase.weight() <= self.__max_weight:
            self.__content.append(suitcase)
            self.__total += suitcase.weight()

    def __str__(self) -> str:
        plural = "suitcase" if len(self.__content) == 1 else "suitcases"
        return f"{len(self.__content)} {plural}, space for {self.__max_weight - self.__total} kg"
    
    def print_items(self):
        for suitcase in self.__content:
            suitcase.print_items()


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()