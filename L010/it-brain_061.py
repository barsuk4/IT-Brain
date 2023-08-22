def remove_line_from_file(filename, line_to_remove):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                if line.strip() != line_to_remove:
                    file.write(line)

        print(f"Рядок '{line_to_remove}' був видалений з файлу '{filename}'.")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    file_name = "test02.txt"  # Вказати назву вашого файлу
    line_to_remove = input("Введіть рядок для видалення: ")
    remove_line_from_file(file_name, line_to_remove)

if __name__ == "__main__":
    main()
