# Итоговая ЛР №8, часть 2
# Основная программа обработки данных

def process_data(filename="data.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Превращаем строки из файла в список чисел
            numbers = [int(line.strip()) for line in f.readlines()]
        
        if not numbers:
            print("Файл пуст.")
            return

        # Алгоритмическая обработка (например, поиск средних значений и фильтрация)
        average = sum(numbers) / len(numbers)
        positive_days = [n for n in numbers if n > 0]

        print(f"Обработано значений: {len(numbers)}")
        print(f"Среднее значение: {average:.2f}")
        print(f"Количество значений выше нуля: {len(positive_days)}")
        
    except FileNotFoundError:
        print("Ошибка: Файл с данными не найден. Сначала запустите generate_data.py")

if __name__ == "__main__":
    process_data()
