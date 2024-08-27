import operations
import math

print("What operation would you like to perform?")
print(" 1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square root\n6. Power\n7. Factorial\n8. Modulus\n9. Logarithm\n10. Exponential")
num = int(input("Enter the number of the operation you would like to perform: "))
if num == 1:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(operations.addition(a, b))
elif num == 2:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(operations.subtraction(a, b))
elif num == 3:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(operations.multiplication(a, b))
elif num == 4:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(operations.division(a, b))
elif num == 5:
    a = int(input("Enter the number: "))
    print(math.sqrt(a))
elif num == 6:
    a = int(input("Enter the base: "))
    b = int(input("Enter the power: "))
    print(math.pow(a, b))
elif num == 7:
    a = int(input("Enter the number: "))
    print(math.factorial(a))
elif num == 8:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(operations.remainder(a, b))
elif num == 9:
    a = int(input("Enter the number: "))
    print(math.log(a))
elif num == 10:
    a = int(input("Enter the number: "))
    print(math.exp(a))
else:
    print("Error. Please enter a valid number.")
    