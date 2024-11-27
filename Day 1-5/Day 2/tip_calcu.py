print("Welcome to tip calculator.")
bill = float(input("What was the total bill?"))
tip_percent = int(input("What percentage tip would you like to give?10, 12 or 15?"))
num_people = int(input("How many people to split the bill?"))
new_bill = bill+bill*tip_percent/100
each_bill = "{:.2f}".format(new_bill/num_people)
print(f"Each person has to pay {each_bill} amount.")