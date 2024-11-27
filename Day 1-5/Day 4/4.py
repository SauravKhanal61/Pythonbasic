row1 = ['😂','😂','😂']
row2 = ['😂','😂','😂']
row3 = ['😂','😂','😂']
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position  = input("enter the index where you want to put the treasure: ")
ver = int(position[0])
hori = int(position[1])
map[hori-1][ver-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")