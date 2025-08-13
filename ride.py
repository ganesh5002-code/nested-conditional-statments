# picking a ride
print("Pick your ride\n1.bike\n2.car")

choice = int(input("\nenter your choice"))

if choice == 1:
    print("What will you chose?\n1.bmx\n2.scooter")
    bike_choice = int(input("\nenter your bike choice:"))
    if bike_choice == 1:
        print("You have chosen a bmx, have a good day")
    else:
        print("You have chosen a scooter, have a good day")
elif choice == 2:
    print("What type of car will you chose?\n1.Hyundai2.Toyota")
    car_choice = int(input("\nenter you car choice:"))
    if car_choice == 1:
        print("You have chosen a Hyundai, have a good day")
    else:
        print("You have chosen a Toyota, have a good day")
else:
    print("This is an invalid choice")