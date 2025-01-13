#11/18/24

#Init

#Functions
def add(num1, num2):
    result = num1+ num2
    print(result)

def sub(num1, num2):
    result = num1 - num2
    print(result)

def mul(num1, num2):
    result = num1*num2
    print(result)

def div(num1, num2):
    result = num1/num2
    print(result)

def simpleCalculator():
    print("Welcome to Simple Calculator")
    while True: #Forever Loop
        print("Please choose an operation")
        print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit""")
        option = input("1-5:")
        if option == str(1):
            num1 = int(input("please enter the first number"))
            num2 = int(input("please enter the second number"))
            add(num1, num2)
        if option == str(2):
            num1 = int(input("please enter the first number"))
            num2 = int(input("please enter the second number"))
            sub(num1, num2)
        if option == str(3):
            num1 = int(input("please enter the first number"))
            num2 = int(input("please enter the second number"))
            mul(num1, num2)
        if option == str(4):
            num1 = int(input("please enter the first number"))
            num2 = int(input("please enter the second number"))
            div(num1, num2)
        if option == str(5):
                print("goodbye")
                break
#Main
simpleCalculator()

