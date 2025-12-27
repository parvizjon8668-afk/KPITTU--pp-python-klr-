# Лабораторная работа №6
# Тема: Функции в Python

def calculate_average(numbers):
    """Функция для вычисления среднего арифметического списка чисел."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_extremes(numbers):
    """Функция для поиска минимального и максимального значений."""
    return min(numbers), max(numbers)

def main():
    # Исходные данные
    data = [15, 42, 7, 23, 90, 11]
    print(f"Входные данные: {data}")

    # Вызов функции для среднего значения
    avg = calculate_average(data)
    print(f"Среднее значение: {avg:.2f}")

    # Вызов функции для поиска экстремумов
    minimum, maximum = find_extremes(data)
    print(f"Минимум: {minimum}, Максимум: {maximum}")

if __name__ == "__main__":
    main()
