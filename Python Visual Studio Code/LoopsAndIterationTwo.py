# NAME: BRANDON L. CAÑETE
# COURSE/YEAR: BSIT - 2ND YEAR
# PROFESSOR: SIR. BRANDO TALAGUIT
# INTEGRATED PROGRAMMING & TECHNOLOGIES 7-8 PM


# Global Variables
Largest = None
Smallest = None

# Function For Large
def Large(Large,Number):
    # if the Large variable has no value
    if Large is None:
    # it will be equal to number variable
        Large = Number
    # if the large variable is less than than the number
    elif Large < Number:
    # it will be equal to number
        Large = Number
    # return the large variable
    return Large

def Small(Smaller,Number):
    # if the smaller variable has no value
    if Smaller is None:
    # it will be equal to number variable
        Smaller = Number
    # if the smaller variable is greater than than the number 
    elif Smaller > Number:
    # it will be equal to number
        Smaller = Number
    # return the smaller variable
    return Smaller

# While Loop so it will run even the user add wrong user input unless it is word "done"
while True:
    # User Input
    number = input("Enter a number: ")
    # For Exit Keyword
    if number == "done":
        break
    if number == "Done":
        break
    if number == "DONE":
        break
    # Try and except so we can catch the user error input
    try:
        # Type Conversion for number variable user input
        Number = int(number)
        # Assign Variables with Logical Functions
        Largest = Large(Largest,Number)
        Smallest = Small(Smallest,Number)
    except:
        # print the error statement 
        print("Invalid Input!")
        # it will just ignore the number
        continue

# print the Largest
print("Maximum is ",Largest)
# print the Smallest
print("Minimum is ",Smallest) 