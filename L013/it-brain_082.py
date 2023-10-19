class KeyIterator:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0
        self.length = len(self.keys)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.length:
            key = self.keys[self.index]
            self.index += 1
            return key
        raise StopIteration

# Приклад використання:
my_dict = {'один': 1, 'два': 2, 'три': 3}
key_iter = KeyIterator(my_dict)

for key in key_iter:
    print(f"Ключ: {key}")
