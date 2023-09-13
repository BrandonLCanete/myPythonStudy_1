hours = None
rate = None
pay = None

try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))
    pay = (hours) * (rate)
    print(pay)
except:
    print("Error, please enter numeric input")
     
