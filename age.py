# checking if the student is between 10 or 20 years old for a class
age = int(input("Enter your age:"))

if age>=10:
    if age<=20:
        print("You are allowed for the class")
    else:
        print("You are not allowed for the class because you are to old")
else:
    print("You are not allowed for the class because you are to young")
