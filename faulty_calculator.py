#This is a "Python Fault Calculator". It does simple mathematical (+,-,*,/) calculation with wrong answer for fixed output values in each operation.

#Code Begins 
result = None

operator = input("Enter a mathematical operator(+,-,*,/): ") 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))

if operator == "+": 
	result = num1 + num2 
	result = result+num1 if result == (5) else result

elif operator == "-": 
	result = num1 - num2

elif operator == "*": 
	result = num1 * num2 
	result = result*num1 if result == (20) else result

elif operator == "/": 
	result = num1 / num2 
	result = result+num2 if result == (4) else result

print("\nThe result is...") 
print(num1, operator, num2, "=", result)
