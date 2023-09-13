# lets make a list in python

# List Variables
List = ["Brandon","Canete",123456789,2580]

# lets make a simple login system using List Variable

# Username variable to hold username question
Username = str(input("What is your username?:"))

# Password variabel to hold password question
Password = int(input("What is your password?:"))

# logic so we can know if the user is the real user of that account

# Heres the logic for the two user
if Username == List[0] and Password == List[2]:
    print("Welcome ",List[0])
elif Username == List[1] and Password == List[3]:
    print("Welcome ",List[1])
# Heres if there is no data for that user
else:
    print("Error,We dont have data of you")
    
