# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__gas = 0
        self.__tacho = 0
    
    def fill_up(self):
        self.__gas = 60

    def drive(self, km: int):
        if self.__gas >= km:
            self.__gas -= km
            self.__tacho += km
        else:
            self.__tacho += self.__gas
            self.__gas = 0

    def __str__(self) -> str:
        return f"Car: odometer reading {self.__tacho} km, petrol remaining {self.__gas} litres"
    
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)