print("Welcome to Python Pizza Delivery")
size = input("What size pizza do you want?S, M, L?")
add_pep = input("Do you want to add pepperoni?Y or N?")
ex_cheese = input ("Do you want extra cheese? Y or N?")
price = 0
if size == "S":
    price +=15
    if add_pep == "Y":
        price +=3
    if add_pep == "Y":
        price += 1
    print(f"Your price is ${price}.")
if size == "M":
    price +=20
    if add_pep == "Y":
        price +=3
    if ex_cheese == "Y":
        price += 1
    print(f"Your price is ${price}.")
if size == "L":
    price +=25
    if add_pep == "Y":
        price +=3
    if ex_cheese == "Y":
        price += 1
    print(f"Your price is ${price}.")
else:
    print("Please choose the Given size")


                   