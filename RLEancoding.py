n = input("Input string: ")
fin = []
i=0
while i<len(n):
    count=1
    while(i+1<len(n) and n[i]==n[i+1]):
        count+=1
        i+=1
    fin.append(n[i])
    fin.append(count)
    i+=1
print(fin)