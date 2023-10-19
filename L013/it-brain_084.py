class EvenIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        if self.current % 2 == 0:
            result = self.current
            self.current += 2  # Переходимо до наступного парного числа
            return result
        else:
            self.current += 1  # Якщо поточне число непарне, переходимо до наступного
            return next(self)  # Рекурсивний виклик для пошуку наступного парного числа

# Приклад використання:
start = 1
end = 10
even_iter = EvenIterator(start, end)

for even_number in even_iter:
    print(even_number)
