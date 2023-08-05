import random

def pick_random_word():
    words = [
        {"word": "apple", "language": "англійською"},
        {"word": "banana", "language": "англійською"},
        {"word": "orange", "language": "англійською"},
        {"word": "grape", "language": "англійською"},
        {"word": "pear", "language": "англійською"},
        {"word": "kiwi", "language": "англійською"},
        {"word": "cherry", "language": "англійською"},
        {"word": "яблуко", "language": "українською"},
        {"word": "банан", "language": "українською"},
        {"word": "апельсин", "language": "українською"},
        {"word": "груша", "language": "українською"},
        {"word": "киві", "language": "українською"},
        {"word": "вишня", "language": "українською"},
    ]
    return random.choice(words)

def hide_word(word, guessed_letters):
    hidden_word = ""
    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter
        else:
            hidden_word += "*"
    return hidden_word

def main():
    word_info = pick_random_word()
    word_to_guess = word_info["word"]
    language = word_info["language"]

    while True:
        max_attempts = input("Введіть кількість спроб для вгадування: ")
        if max_attempts.isdigit():
            max_attempts = int(max_attempts)
            break
        else:
            print("Некоректне значення. Введіть ціле число.")

    guessed_letters = set()
    correct_letters = set(word_to_guess)

    print(f"Вгадайте слово {language}:")
    print(hide_word(word_to_guess, guessed_letters))

    while max_attempts > 0:
        guess = input("Введіть літеру або слово: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Ви вже вводили цю літеру")
            else:
                guessed_letters.add(guess)
                hidden_word = hide_word(word_to_guess, guessed_letters)
                print(hidden_word)

                if guessed_letters == correct_letters:
                    print("Вітаю, ви вгадали слово!")
                    break
        elif guess.isalpha():
            if guess == word_to_guess:
                print("Вітаю, ви вгадали слово!")
                break
            else:
                print("Слово не правильне")
        else:
            print("Будь ласка, введіть тільки літери або слово.")

        max_attempts -= 1

    if max_attempts == 0:
        print("Ви програли. Спробуйте ще раз!")

if __name__ == "__main__":
    main()

