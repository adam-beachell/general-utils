import operator

# Available operations
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# Prompt for numbers with validation
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

# Print menu for user
def show_menu():
    print("\nSimple Calculator CLI")
    print("Available operations:")
    for symbol in ops:
        print(f"  {symbol}  -> {ops[symbol].__name__}")
    print("Type 'q' or 'quit' to exit.\n")

# Main calculator loop
def calculator():
    while True:
        show_menu()
        op = input("Enter operation: ").strip()

        if op.lower() in ('q', 'quit'):
            print("Goodbye!")
            break
        elif op in ops:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if op == '/' and num2 == 0:
                print("Cannot divide by zero.")
                continue

            try:
                result = ops[op](num1, num2)
                print(f"Result: {num1} {op} {num2} = {result}\n")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Unknown operation. Please try again.")

# Run the calculator
if __name__ == "__main__":
    calculator()