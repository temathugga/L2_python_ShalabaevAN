# Программа 1
import random
random_number = random.randint(1, 100)
print("Случайное число от 1 до 100:", random_number)

# Программа 2
from datetime import datetime
current_time = datetime.now()
print("Текущая дата и время:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# Программа 3
import math
number = float(input("Введите число: "))
sqrt_value = math.sqrt(number)
print(f"Квадратный корень числа {number}: {sqrt_value}")

# Программа 4
def sqrt_without_math(number):
    if number < 0:
        raise ValueError("Нельзя вычислить квадратный корень отрицательного числа.")
    if number == 0:
        return 0

    guess = number / 2
    while True:
        new_guess = (guess + number / guess) / 2
        if abs(new_guess - guess) < 1e-9:  # Проверяем точность
            return new_guess
        guess = new_guess

number = float(input("Введите число: "))
sqrt_value = sqrt_without_math(number)
print(f"Квадратный корень числа {number}: {sqrt_value}")
