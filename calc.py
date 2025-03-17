expression = input("Введите выражение (например, 2 + 2): ")
num1, operator, num2 = expression.split()
num1 = float(num1)
num2 = float(num2)

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Неверный оператор")
  
