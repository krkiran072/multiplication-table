class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b


def main():
    calc = Calculator()

    print("=== Simple Calculator ===")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Error! Please enter valid numbers.")
        return

    print("Choose operation: +  -  *  /")
    op = input("Enter operator: ").strip()

    if op == "+":
        result = calc.add(a, b)
    elif op == "-":
        result = calc.subtract(a, b)
    elif op == "*":
        result = calc.multiply(a, b)
    elif op == "/":
        result = calc.divide(a, b)
    else:
        print("Error! Invalid operator.")
        return

    print("Result:", result)


if __name__ == "__main__":
    main()
