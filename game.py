import random
secret_number = random.randint(0, 10)
attempts = 3
print("Угадай число от 0 до 10! У тебя 3 попытки.")
for attempt in range(attempts):
    guess = int(input(f"Попытка {attempt + 1}. Введи число: "))

    if guess == secret_number:
        print("Поздравляю! Ты угадал!")
        break
    elif guess < secret_number:
        print("Неверно! Загаданное число больше.")
    else:
        print("Неверно! Загаданное число меньше.")
else:
    print(f"Ты проиграл! Загаданное число было: {secret_number}.")
