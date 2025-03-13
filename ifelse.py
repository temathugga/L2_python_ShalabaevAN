# Программа 1
user_input = int(input("Введите число: "))
if user_input % 2 == 0:
    print("Ваше число чётное")
else:
    print('Ваше число нечётное')

# Программа 2
user_number1 = int(input('Введите первое число: '))
user_number2 = int(input('Введите второе число: '))
if user_number1 > user_number2:
    print(f"Первое число: {user_number1} больше.")
else:
    print(f"Второе число: {user_number2} больше.")

# Программа 3
age = int(input("Введите ваш возраст: "))
if age >= 18:
    print("Вы можете получить водительские права.")
else:
    print("Вы не достигли 18 летнего возраста для получения прав.")
