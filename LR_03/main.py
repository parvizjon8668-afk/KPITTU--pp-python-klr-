# Лабораторная работа №3
# Словари, множества, функции

# ---------------------------------
# Задача 1. Email-анализ
# ---------------------------------
emails = [
    "student1@gmail.com",
    "student2@yandex.ru",
    "student3@gmail.com",
    "student4@mail.ru",
    "student5@gmail.com",
    "student6@yandex.ru"
]

# Выделение доменов
domains = []
for email in emails:
    domain = email.split("@")[1]
    domains.append(domain)

# Подсчёт частот доменов
freq = {}
for d in domains:
    if d in freq:
        freq[d] += 1
    else:
        freq[d] = 1

# Определение самого популярного домена
max_domain = None
max_count = 0

for d in freq:
    if freq[d] > max_count:
        max_count = freq[d]
        max_domain = d

print("Домены:", domains)
print("Частоты доменов:", freq)
print("Самый популярный домен:", max_domain)

print("-" * 40)

# ---------------------------------
# Задача 2. Генератор отчётов о студентах
# ---------------------------------
students = [
    {"name": "Ali", "score": 87, "group": "A"},
    {"name": "Habib", "score": 78, "group": "B"},
    {"name": "Umar", "score": 92, "group": "A"},
]

def report(students, fields=["name", "score"], sort_by="score", reverse=False):
    sorted_students = sorted(students, key=lambda s: s[sort_by], reverse=reverse)
    for s in sorted_students:
        parts = []
        for f in fields:
            parts.append(str(s[f]))
        print(": ".join(parts))

print("Отчёт студентов:")
report(
    students,
    fields=["name", "score"],
    sort_by="score",
    reverse=True
)
