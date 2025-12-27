# Итоговая ЛР №8, часть 2
# Скрипт для генерации синтетических данных

import random

def generate_data(filename="data.txt"):
    # Генерируем список случайных чисел (например, показатели температуры)
    data = [random.randint(-20, 35) for _ in range(20)]
    
    with open(filename, "w", encoding="utf-8") as f:
        for item in data:
            f.write(f"{item}\n")
    print(f"Файл {filename} успешно создан с {len(data)} записями.")

if __name__ == "__main__":
    generate_data()
