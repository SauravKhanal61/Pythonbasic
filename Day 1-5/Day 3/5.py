your_name = input("Enter your name:")
her_name = input("Enter her name:")
your_name = your_name.lower()
her_name = her_name.lower()
true = your_name.count("t") + your_name.count("r") + your_name.count("u") + your_name.count("u")
true*=2
true = str(true)
love = her_name.count("l") + her_name.count("o") + her_name.count("v") + her_name.count("e")
love = str(love)
true_love = true+love
true_love = int(true_love)
if(true_love < 10 or true_love > 90):
    print(f"your score is {true_love}. You go like mentos and cola.")
elif(true_love>40 and true_love<50):
    print(f"your score is {true_love}. You are alright together.")
else:
    print(f"your score is {true_love}.")