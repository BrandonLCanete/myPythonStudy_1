Largest = None
Smallest = None

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        Number = int(number)
        if Largest is None:
            Largest = Number
        elif Largest < Number:
            Largest = Number
        if Smallest is None:
            Smallest = Number
        elif Smallest > Number:
            Smallest = Number
    except:
        print("Invalid input")
       
print("Maximum is ",Largest)
print("Minimum is ",Smallest) 