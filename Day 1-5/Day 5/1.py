height = input("Enter the list of student heights:").split()
i = 0
for n in range(0,len(height)):
    height[n] = int(height[n])
    i+=1
print(height)
sum = 0;
for n in range(0,i):
    sum += height[n]
avg = sum/len(height)
print(f"Average height is {(round(avg))}")