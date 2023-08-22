def write_to_file(filename, content):
    try:
        with open(filename, 'x') as file:
            file.write(content)
        print(f"Рядок було успішно записано у файл '{filename}'.")
    except FileExistsError:
        new_filename = input(f"Файл '{filename}' вже існує. Введіть нове ім'я файлу: ")
        write_to_file(new_filename, content)
    except Exception as e:
        print(f"Виникла помилка при записі у файл: {e}")

def main():
    user_input = input("Введіть рядок для запису у файл: ")
    filename = input("Введіть назву файлу для запису: ")
    write_to_file(filename, user_input+"\n")

if __name__ == "__main__":
    main()
