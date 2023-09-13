# NAME: BRANDON L. CAÑETE
# COURSE/YEAR: BSIT - 2ND YEAR
# PROFESSOR: SIR. BRANDO TALAGUIT
# INTEGRATED PROGRAMMING & TECHNOLOGIES 7-8 PM

# Iteration Variables
Letter_Count = 0
Digit_Count = 0

# Function for Letter
def Function_Letter(Letter_Count):
    # For loop count variable that will take the user variable so that we can access the user input
    for count in user:
        # if statement to check whether the count variable isalpha method meaning it will check all alphabet letters in the user input
        if count.isalpha():
            # Increment the letter count variable so it will count the alphabet letters in the user input
            Letter_Count += 1
    # return the letter count variable so we can get the value for this function
    return Letter_Count

# Funtion for Digit
def Function_Digit(Digit_Count):
    # For loop count variable that will take the user variable so that we can access the user input
    for count in user:
        # if statement to cehck whether the count variable isdigit method meaning it will check all the digit numbers in the user input
        if count.isdigit():
            # Increment the digit count variable so it will count the digit numbers in the user input
            Digit_Count += 1
    # return the digit count variable so we can get the value for this function
    return Digit_Count

# Lets user try and except so we can get the error for user input
try:
    # user string variable that holds the user question
    user = str(input("Enter Username: "))
    # letters and digits variable that will hold the function for letter and digit counts
    Letters = Function_Letter(Letter_Count)
    Digits = Function_Digit(Digit_Count)
except:
    # error message
    print("Invalid, Input!")

# print the Letter and Digit counts
print("Letters = ",Letters,",Digits = ",Digits)