# lets make a python program where we will gonna take Employee Salary

# Global variables so we can use it everywhere
a = None 
b = None
c = None
d = None
e = None
f = None
g = None
h = None
i = None
j = None
k = None
l = None
m = None
n = None
o = None

# lets make a function where it will calculate the total
def calculate_total(total1,total2):
    # here we do a variables total1 and total2 where it will time a and b and the rest variables will be plus 
    total1 = a * b + c + d + e + f + g
    total2 = h + i + j + k + l + m + n + o
    # here we make a variable result that hold the total1 - total2
    result = total1 - total2
    # and we return the result variable so we can get its value
    return result

# We try and except here so we can catch the error if there is a invalid input user
try:
    # We make here a questioner data
    print("Gross Income Components:\n")
    a = int(input("How much is your Rate Per Day?:"))
    b = int(input("How many is your total No. of Work days?:"))
    c = int(input("How much is your Honorarium?:"))
    d = int(input("How much is your Incentives?:"))
    e = int(input("How much is your Over time Pay?:"))
    f = int(input("How much is your Meal Allowance?:"))
    g = int(input("How much is your Transportation Allowance?:"))
    print("\nTotal Deductions:\n")
    h = int(input("How much is your SSS ?:"))
    i = int(input("How much is your Phil-Health?:"))
    j = int(input("How much is your Pag-Ibig?:"))
    k = int(input("How much is your Tax?:"))
    l = int(input("How many is your Cash Advance?:"))
    m = int(input("How many is your Late?:"))
    n = int(input("How many is your Absent?:"))
    o = int(input("How much is your Loan?:"))

except:
    # here is the error message if the user add an invalid input
    print("Error, There is a problem with your data input")
    exit(0)


# Now we make a variable total1 so we can calculate the Gross Income and also print the total
Gross_Income = a * b + c + d + e + f + g
print("\nThe total Gross Income is:",Gross_Income)

# Now we make a variable total2 so we can calculate the total Deduction and also print the total
Total_Deduction = h + i + j + k + l + m + n + o
print("The total Deduction is:",Total_Deduction)

# Now we will call the calculate_total function and add the total1 and total2 inside it to be parameters and get the total Net Income and print the total
Net_Income = calculate_total(Gross_Income,Total_Deduction)
print("The total Net Income is:",Net_Income)
	
		 
		 
		  
		 
		  
		  
		 