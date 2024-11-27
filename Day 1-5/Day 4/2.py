import random
print("Play head or tail")
input = input("Enter your choice?H or T?")
ran_toss = random.randint(0,1)
# if ran_toss==1:
#     if input == "H":
#         print("Its head you won")
#     else:
#         print("Its tail You lose")
# else:
#     if input == "T":
#         print("Its tail you won")
#     else:
#         print("Its head You lose")
toss = ["H","T"]
if(input == toss[ran_toss]):
    print("you win")
else:
    print("You lose")