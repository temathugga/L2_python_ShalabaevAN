# Программа 1
try:
    number = float(input("Введите число: "))
    print(f"Вы ввели число: {number}")
except ValueError:
    print("Ошибка: Введено не число!")

# Программа 2
filename = input("Введите имя файла: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Ошибка: Файл '{filename}' не существует!")
