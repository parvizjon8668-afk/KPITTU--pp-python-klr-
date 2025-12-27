# Лабораторная работа №2
# Циклы, строки, list comprehension

# -------------------------------
# Задача 1. Удалить все пробелы, кроме первого
# -------------------------------
text = input("Введите строку: ")

result = ""
first_space = False

for char in text:
    if char == " ":
        if first_space:
            continue
        else:
            result += char
            first_space = True
    else:
        result += char

print("Результат:", result)

print("-" * 40)

# -------------------------------
# Задача 2. Проверка знакопеременной последовательности
# -------------------------------
nums = input("Введите числа через пробел: ").split()

try:
    numbers = [int(x) for x in nums]
    if len(numbers) <= 1:
        print("да")
    else:
        prev_sign = numbers[0] > 0
        ok = True

        for x in numbers[1:]:
            current_sign = x > 0
            if current_sign == prev_sign:
                ok = False
                break
            prev_sign = current_sign

        if ok:
            print("да")
        else:
            print("нет")
except ValueError:
    print("Ошибка ввода данных")

print("-" * 40)

# -------------------------------
# Задача 3. Статистика строки
# -------------------------------
text = input("Введите строку для анализа: ")

letters = [c for c in text if c.isalpha()]
digits = [c for c in text if c.isdigit()]
spaces = [c for c in text if c == " "]
others = [c for c in text if not c.isalpha() and not c.isdigit() and c != " "]

print("Буквы:", len(letters))
print("Цифры:", len(digits))
print("Пробелы:", len(spaces))
print("Другие символы:", len(others))
