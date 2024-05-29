# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __value(self):
        return self.__euros * 100 + self.__cents
    
    def __set_value(self, cents: int):
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100
    
    def __eq__(self, another: "Money"):
        return self.__value() == another.__value()
    
    def __gt__(self, another: "Money"):
        return self.__value() > another.__value()

    def __lt__(self, another: "Money"):
        return self.__value() < another.__value()

    def __ne__(self, another: "Money"):
        return self.__value() != another.__value()
    
    def __add__(self, another: "Money"):
        result = Money(0, 0)
        result.__set_value(self.__value() + another.__value())
        return result
    
    def __sub__(self, another: "Money"):
        result = Money(0, 0)
        result.__set_value(self.__value() - another.__value())
        if result.__value() < 0:
            raise ValueError("a negative result is not allowed")
        return result
        
       

if __name__ == "__main__":
    e1 = Money(1, 1)
    e2 = Money(1, 1)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1