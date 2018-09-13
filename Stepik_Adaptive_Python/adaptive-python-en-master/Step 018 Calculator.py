operations = {"+": lambda x, y: x + y,
              "-": lambda x, y: x - y,
              "/": lambda x, y: x / y,
              "*": lambda x, y: x * y,
              "mod": lambda x, y: x % y,
              "pow": lambda x, y: x ** y,
              "div": lambda x, y: x // y}

a = float(input())
b = float(input())
op = input()

try:
    print(operations[op](a, b))  # dictionary nested with op as key and a lambda function as value

except ZeroDivisionError:
    print("Division by 0!")
