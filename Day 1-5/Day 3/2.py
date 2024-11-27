height = int(input("Enter your height?"))
bill =0
if height>=120:
    age = int(input("Enter your age."))
    if(age <= 12):
        print("Price is $5.")
        bill = 5
    elif(age<18):
        print("Price is $7.")
        bill = 7
    elif(age >=45 and age<=55):
        print("Everything is going to be OK ride is on us.")
    else:
        print("Price is $12.")
        bill = 12
    
    photo = input("Do you want to take a photo? Y or N?")
    if photo == "Y":
        bill += 3

    print(f"You have to pay ${bill}.")
else:
    print("You have to grow taller for the ride.")
