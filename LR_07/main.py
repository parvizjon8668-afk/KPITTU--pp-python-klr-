# Лабораторная работа №7
# Тема: Работа с файлами в Python

def main():
    file_name = "data.txt"
    content_to_write = "Это тестовая строка для записи в файл.\nЛабораторная работа №7 выполнена."

    # 1. Запись данных в файл
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content_to_write)
        print(f"Данные успешно записаны в файл: {file_name}")
    except Exception as e:
        print(f"Ошибка при записи: {e}")

    # 2. Чтение данных из файла
    print("\nЧтение содержимого файла:")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Ошибка при чтении: {e}")

if __name__ == "__main__":
    main()
