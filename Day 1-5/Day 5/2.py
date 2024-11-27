marks = input("enter the different height:").split()
for n in range(0,len(marks)):
    marks[n] = int(marks[n])
print(marks)
highest = marks[0]
for n in range(0,len(marks)):
    if marks[n]>=highest:
        highest = marks[n]
print(f"Hightest ={highest}")
