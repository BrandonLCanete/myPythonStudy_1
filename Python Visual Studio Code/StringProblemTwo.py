# NAME: BRANDON L. CAÑETE
# COURSE/YEAR: BSIT - 2ND YEAR
# PROFESSOR: SIR. BRANDO TALAGUIT
# INTEGRATED PROGRAMMING & TECHNOLOGIES 7-8 PM


# Function for Change position of the user input
def change_Position(position):
    # We will slice the position variable to change the position of the user input first and last characters
    position =  position[-1:] + position[1:-1] + position[:1]
    # return the variable position so we can get the value
    return position


# Lets use try and except so we can get the error message for the user input
try:
    # user variable that holds the user question
    user = input("Enter Message: ")
    # position variable that holds the change position function
    position = change_Position(user)
except:
    # error message
    print("Invalid, Input!")

# print the position variable
print(position)