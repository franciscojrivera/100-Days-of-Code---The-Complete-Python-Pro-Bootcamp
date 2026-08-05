def add(n1, n2):
    return n1 + n2

# TODO: Write out the other three functions - subtract, multiply, and divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary\
calc = "n"
loop = True
while loop == True:
    if calc == "n":
        n1 = int(input("What is the first number?: "))
        operator = input("What is the operator?: ")
        n2 = int(input("What is the second number?: "))
        result = operations[operator](n1, n2)
    else:
        operator = input("What is the operator?: ")
        n2 = int(input("What is the second number?: "))
        result = operations[operator](n1, n2)

    print(f"{n1} {operator} {n2} = {result}")

    calc = input(f"Do you want to continue calculating with {result} (y/n): ")
    if calc == "y":
        n1 = result




