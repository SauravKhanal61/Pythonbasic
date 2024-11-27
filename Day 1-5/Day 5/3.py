sum = 0 
num1 = int(input("Enter the first even number:"))
num2 = int(input("Enter the last even number"))
for n in range(num1,num2+1,2):
    sum+=n
print(sum)