def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = set(line.strip() for line in f1.readlines())
            lines2 = set(line.strip() for line in f2.readlines())
        
        lines_difference = lines1 - lines2
        
        print(f"Рядки, які є в файлі '{file1}', але відсутні в файлі '{file2}':")
        for line in lines1:
            if line in lines_difference:
                print(line)
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
