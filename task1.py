
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
operator = input("Enter operation (+, -, *, /): ")

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print("Error: Division by zero!")
    else:
        print(num1 / num2)
else:
    print('Invalid operator')

print('Thank you')
