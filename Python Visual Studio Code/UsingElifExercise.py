score = input("Enter Score: ")

Score = float(score)


if Score >= 0.9 and Score <=1.0:
    print("Your Grade is A")
elif Score >= 0.8 and Score <=0.9:
    print("Your Grade is B")
elif Score >= 0.7 and Score <=0.8:
    print("Your Grade is C")
elif Score >= 0.6 and Score <=0.7:
    print("Your Grade is D")
elif Score >=0.0 and Score < 0.6:
    print("Your Grade is F")
else:
    print("Error Score!")