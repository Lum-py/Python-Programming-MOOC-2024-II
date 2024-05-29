# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
 
class Room:
    def __init__(self):
        self.room = []

    def add(self, person: Person):
        self.room.append(person)        

    def is_empty(self):
        return len(self.room) == 0
    
    def print_contents(self):
        if not self.is_empty():
            self.total = sum(person.height for person in self.room)
            print(f"There are {len(self.room)} persons in the room, and their combined height is {self.total} cm")
            for person in self.room:
                print(person.name, f"({person.height} cm)")

    def shortest(self):
        if self.is_empty():
            return None
        short = self.room[0]
        for person in self.room[1:]:
            if person.height < short.height:
                short = person
        return short

    def remove_shortest(self):
        if not self.is_empty():
            removed = self.shortest()
            self.room.remove(removed)
            return removed   
        return None

if __name__ == "__main__":
    room = Room()
    room.add(Person("Grace", 180))
    room.add(Person("Jan", 175))
    room.add(Person("Lisa", 150))
    room.add(Person("Paul", 204))
    room.add(Person("Jana", 171))
    room.add(Person("Ruth", 149))
    room.print_contents()
    print()
    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()

    '''
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
    '''