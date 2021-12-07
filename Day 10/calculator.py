from logo import logo
import os

os_clear = 'cls' if os.name == 'nt' else 'clear'


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    should_continue = True

    while should_continue:
        while True:
            for symbol in operations:
                print(symbol)
            operator = input("Choose an operation to perform: ")

            if operator not in operations.keys():
                print("Choose only the valid operators: \n")
                continue
            break


        num2 = float(input("Enter the next number: "))
        result = operations[operator](num1, num2)

        print(f"{num1} {operator} {num2} = {result} ")

        should_continue = input(f"""Type 'y' to continue calculating with the answer {result}:
        or, type 'n' to start a new calculator""").lower()
        if should_continue == 'y':
            num1 = result
            continue
        elif should_continue == 'n':
            os.system(os_clear)
            calculator()
        
        return 

calculator()