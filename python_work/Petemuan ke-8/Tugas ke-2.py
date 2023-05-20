#Tugas ke-2

number = [71, 73, 72, 74, 76, 70, 68, 78, 71, 70]

numMean = sum(number) / len(number)

for i in number:
    if i > numMean:
        print(i)