# Write your solution here
def even_numbers(beginning: int, maximum: int):    
    yield from (num for num in range(beginning, maximum + 1) if num % 2 == 0)

if __name__ == "__main__":
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)