# NAME: BRANDON L. CAÑETE
# COURSE/YEAR: BSIT - 2ND YEAR
# PROFESSOR: SIR. BRANDO TALAGUIT
# INTEGRATED PROGRAMMING & TECHNOLOGIES 7-8 PM


# Assign Variables
counts = 0
totals = 0
averages = 0

# Function for Count
def Count(count):
    # Calculate the Value for Count
    count = count + 1
    return count

# Function For Total
def Total(total,Number):
    # Calculate the Value for Total
    total = total + Number
    return total

# Function For Average
def Average(total,count):
    # Calculate the Value for Average
    average = total / count
    return average

# While Loop so it will run even the user add wrong user input unless it is word "done"
while True:
    # User Input
    number = input("Enter a number: ")
    # For exit keyword
    if number == "done":
        break
    if number == "DONE":
        break
    if number == "Done":
        break
# try and except so we can catch user invalid input
    try:
        # Type Conversion for number variable user input
        Number = int(number)
        # Assign Variables with Logical Functions
        counts = Count(counts)
        totals = Total(totals,Number)
        averages = Average(totals,counts)
    except:
        # Error Statement
        print("Invalid Input!")
        # continue so it will just skip the error message
        continue

# print the total, count and average
print(totals ,counts ,averages)