def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = set(line.strip() for line in f1.readlines())
            lines2 = set(line.strip() for line in f2.readlines())
        
        lines_difference_1_to_2 = lines1 - lines2
        lines_difference_2_to_1 = lines2 - lines1
        
        result = {}
        for line in lines_difference_1_to_2:
            result[line] = f"'{file1}' -> '{file2}'"
        for line in lines_difference_2_to_1:
            result[line] = f"'{file2}' -> '{file1}'"
        
        print(f"Результат порівняння між файлами '{file1}' та '{file2}':")
        if not result:
            print("Файли містять однаковий вміст.")
        else:
            for line, direction in result.items():
                print(f"{line}: {direction}")
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def main():
    file1 = input("Введіть назву першого файлу: ")
    file2 = input("Введіть назву другого файлу: ")
    compare_files(file1, file2)

if __name__ == "__main__":
    main()
