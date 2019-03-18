file = open("dane_systemy1.txt")
data1 = file.readlines()
for i, line in enumerate(data1):
    data1[i] = line.rstrip().split(' ')
file = open("dane_systemy2.txt")
data2 = file.readlines()
for i, line in enumerate(data2):
    data2[i] = line.rstrip().split(' ')
file = open("dane_systemy3.txt")
data3 = file.readlines()
for i, line in enumerate(data3):
    data3[i] = line.rstrip().split(' ')
counter = 0
for i in range(0, len(data1)-1):
    if(int(data1[i][0],2)%12!=0 and int(data2[i][0],4)%12!=0 and int(data3[i][0],8)%12!=0):
        counter += 1
print(counter)