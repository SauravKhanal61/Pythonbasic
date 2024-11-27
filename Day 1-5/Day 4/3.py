import random
name_str = input("Enter the names seperated by comma',':")
name = name_str.split(", ")
# len = len(name)
# ran = random.randint(0,len-1)

print(f"{random.choice(name)} will pay the bill")