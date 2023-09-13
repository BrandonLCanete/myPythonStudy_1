# NAME: BRANDON LEONCITO CAÑETE
# COURSE/YEAR: BSIT - 2ND YEAR
# PROFESSOR: SIR. BRANDO TALAGUIT
# INTEGRATED PROGRAMMING TECHNOLOGIES 7 - 8 PM

# Global Variables so we can accessed it even outside of the function
hours = None
rate = None
pay = None

# function computepay that handles the logic of the program
def computepay(hours,rate):
    # Check if the hours are less than or equal to 40.
    if hours <= 40:
        pay = hours * rate
    else:
        # If the hours are greater than 40, calculate the overtime hours and overtime rate.
        pay = (( hours - 40 ) * ( 1.5 * rate )) + (40 * rate)
        #overtime_hours = hours - 40
        #overtime_rate = rate * 1.5

        # Calculate the pay for normal hours and the pay for overtime 
        #normal_pay = 40 * rate
        #overtime_pay = overtime_hours + overtime_rate

        # Add the pay for normal hours and the pay for overtime to get the total pay
        #pay = normal_pay + overtime_pay
    
    # Return the total pay
    return pay

# The main so we can run the program and also we try and except it so even if the user add wrong data it will atleast catch the error
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    pay = computepay(hours,rate)
    print("Pay: ", pay)
except:
    print("Error, There is wrong with your data input!")


    