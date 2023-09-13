hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

Hours = int(hours)
Rate = int(rate)

if Hours <= 40:
    Pay = Hours * Rate
else:
    Pay = (( Hours - 40 ) * ( 1.5 * Rate )) + (40 * Rate)

print("Pay: ", Pay)