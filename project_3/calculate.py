# define the function needed, add, sub, mul, div
# print option to the user
# ask for value
# call the functions
# while loop to continue the program until the user want to exit


def addition(a, b):
    answer = a + b
    print(f"\n\t {a} + {b} = {answer}  \n")


def subtraction(a, b):
    answer = a - b
    print(f"\n \t {a} - {b} = {answer}  \n")


def multipliation(a, b):
    answer = a * b
    print(f"\n \t {a} * {b} = {answer}  \n")


def division(a, b):
    answer = a / b
    print(f"\n \t {a} / {b} = {answer}  \n")


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ").upper()

    if choice == "A":
        print("Addition")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        addition(a, b)
    elif choice == "B":
        print("Subtraction")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        subtraction(a, b)
    elif choice == "C":
        print("Multiplication")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        multipliation(a, b)
    elif choice == "D":
        print("Division")
        a = int(input("input first number: "))
        b = int(input("input second number: "))
        division(a, b)
    elif choice == "E":
        print("Program ended")
        quit()
