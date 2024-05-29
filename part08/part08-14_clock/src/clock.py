# Write your solution here:
class Clock:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def tick(self):
        self.second += 1
        if self.second > 59:
            self.second = 0
            self.minute +=1
            if self.minute > 59:
                self.minute = 0
                self.hour += 1
                if self.hour > 23:
                    self.hour = 0

    def __str__(self) -> str:
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
    
    def set(self, hours, minutes):
        self.hour = hours
        self.minute = minutes
        self.second = 0

    

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
