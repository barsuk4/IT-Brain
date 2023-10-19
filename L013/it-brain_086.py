class PalindromeIterator:
    def __init__(self, words):
        self.words = words
        self.current_word = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_word < len(self.words):
            word = self.words[self.current_word]
            self.current_word += 1
            if word.lower() == word.lower()[::-1]:
                return word
        raise StopIteration

# Приклад використання:
word_list = ["рівень", "радар", "Анна", "сон", "парк"]
palindrome_iter = PalindromeIterator(word_list)

for palindrome in palindrome_iter:
    print(palindrome)
