def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
            with open(destination_file, 'a') as destination:
                destination.write(content)
        print(f"Вміст файлу '{source_file}' було успішно додано до файлу '{destination_file}'.")
    except FileNotFoundError:
        print(f"Файл '{source_file}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка при копіюванні файлу: {e}")

def main():
    source_file = input("Введіть назву вихідного файлу: ")
    destination_file = input("Введіть назву файлу призначення: ")
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
