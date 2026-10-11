n = input("Input string to decode: ")
fin = []
i=0
while i<len(n):
    letter = n[i]
    count = int(n[i+1])

    for a in range(count):
        fin.append(letter)

    i+=2

print(fin)