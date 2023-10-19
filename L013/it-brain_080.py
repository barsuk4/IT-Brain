class CharIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.text):
            char = self.text[self.index]
            self.index += 1
            return char
        raise StopIteration

# Приклад використання:
text = "Це є тестовий рядок"
char_iter = CharIterator(text)

for char in char_iter:
    print(char)
