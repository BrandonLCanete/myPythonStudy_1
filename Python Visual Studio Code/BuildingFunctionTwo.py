# NAME: BRANDON LEONCITO CAÑETE
# COURSE/YEAR: BSIT - 2ND YEAR
# PROFESSOR: SIR. BRANDO TALAGUIT
# INTEGRATED PROGRAMMING TECHNOLOGIES 7 - 8 PM

# Global Variables so we can accessed it even outside of the function
score = None

# function computegrade that handles the logic of the program
def computegrade(score):
    if score > 1.0 or score < 0.0: 
        return "Bad score"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8: 
        return "B"
    elif score >= 0.7: 
        return "C"
    elif score >= 0.6: 
        return "D"
    else: 
       return "F"
    #if score >= 0.9 and score <=1.0:
        #return "A"
    #elif score >= 0.8 and score <=0.9:
        #return "B"
    #elif score >= 0.7 and score <=0.8:
        #return "C"
    #elif score >= 0.6 and score <=0.7:
        #return "D"
    #elif score >=0.0 and score < 0.6:
        #return "F"
    #else:
    #    return "Bad score"

# The main so we can run the program and also we try and except it so even if the user add wrong data it will atleast catch the error
try:
    score = float(input("Enter Score: "))
except:
    print("Bad score")
    exit()

grade = computegrade(score)
print(grade)