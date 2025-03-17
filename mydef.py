# Программа 1
def sum_two_numbers(a, b):
    return a + b
result = sum_two_numbers(5, 3)
print("Сумма чисел:", result)  

# Программа 2
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 29
if is_prime(number):
    print(f"{number} — простое число.")
else:
    print(f"{number} — не простое число.")

# Программа 3
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  
    return sum(numbers) / len(numbers)
numbers_list = [10, 20, 30, 40, 50]
average = calculate_average(numbers_list)
print("Среднее значение:", average) 
