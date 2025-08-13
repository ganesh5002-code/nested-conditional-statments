# Checking if a student is eligible for a test
med = str(input("Are you medically fit for the test, yes or no:"))
atten = int(input("Have you attended the required number of classes, yes or no:"))

if med == "no":
    print("You are eligible for the test")
else:
    if atten >= 75:
        print("You are eligible for the test")
    else:
        print("You are not eligible for the test")