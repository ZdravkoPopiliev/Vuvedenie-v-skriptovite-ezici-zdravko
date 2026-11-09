n = int(input("Input number: "))
if n==0:
    print("Invalid number.")

a = []

for i in range(n):
    num = int(input())
    a.append(num)

devis = 0
evenSum = 0
evenNum = 0

for i in range(0,n):
    if a[i]%3==0:
        devis += 1
    if a[i]>0:
        evenSum+=a[i]
        evenNum+=1

print("Devsible by 3:", devis)
avr = evenSum/evenNum
print("Avereage(+numbers):",avr)

