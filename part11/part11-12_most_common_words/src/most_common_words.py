# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    word_count = {}
    with open(filename) as file:
        for line in file:
            words = line.strip().split() 
            for word in words:
                word = word.rstrip('.,!?')
                word_count[word] = word_count.get(word, 0) +1

    return {word: count for word, count in word_count.items() if count >= lower_limit}

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))