# Simple Calculator with python

# lets make a Global variable so that it can enter the function normally
num1 = None
num2 = None

# lets make a function where it will return a addition value
def addition_function(num1,num2):
    # lets make a add variable so we can add the num1 and num2 parameters
    add = num1 + num2
    # lets return it so we can get the addition_function value
    return add

# lets also make a function where it will return a subtraction value
def subtraction_function(num1,num2):
    # lets make a minus variable so we can minus the num1 and num2 parameters
    minus = num1 - num2
    # lets return it so we can get the subtraction_function value
    return minus

# lets also make a function where it will return a multiplication value
def multiplication_function(num1,num2):
    # lets make a times variable so we can times the num1 and num2 parameters
    times = num1 * num2
    # lets return it so we can get the multiplication_function value
    return times

# lastly we also need to make a function where it will return a division value
def division_function(num1,num2):
    # lets make a divide variable so we can divide the num1 and num2 parameters
    divide = num1 / num2
    # lets return it so we can get the division_function value
    return divide

# lets while true it so that it will still run even if the symbol is incorrect unless the user add invalid data the program will exit
while True:
# lets try and except the main so if the user input is invalid it will catch it and says error message
    try:
    # lets make a num1 variable that will hold the data for user question
        num1 = int(input("What is your First number?:"))
    # lets make a symbol variable so that the program will know if its add, subtract , multiply or division
        symbol = str(input("What is your Calculator Symbol (+,-,*,/):"))
    # lets also make a num2 variable so that there will be a second question so that we can add , subtract , multiply or divide it
        num2 = int(input("What is your Second number?:"))
    except:
    # We will catch the error if the user input is invalid
        print("Error, The program will exit")
        exit(0)

# lets a make a logic so if the user choose the symbol + it will print the addition_function
    if symbol == "+":
# lets make a variable that will hold the addition_function so that we can print the addition value
        addition = addition_function(num1,num2)
# print the output
        print(addition)

# lets make a logic so if the user choose the symbol - it will print the subtraction_function
    elif symbol == "-":
# lets make a variable that will hold the subtraction_function so that we can print the subtraction value
        subtract = subtraction_function(num1,num2)
# print the output
        print(subtract)

# lets make a logic so if the user choose the symbol * it will print the multiplication_function
    elif symbol == "*":
# lets make a variable that will also hold the multiplication_function so that we can print the multiplication value
        multiply = multiplication_function(num1,num2)
# print the output
        print(multiply)

# lets make a logic so if the user choose the symbol / it will print the division_function
    elif symbol == "/":
# lastly lets make a variable that will hold the division_function so that we can print the division value
        division = division_function(num1,num2)
# print the output
        print(division)

# lets make a logic if the user symbol is not on the list it will print a error message
    else:
        print("Wrong symbol, Please Try Again!")
    