#Въвеждат се цели числа, всяко на отделен ред, докато не се въведе 0. Нулата не е част от редицата.
#а) (6 т.) Прочетете числата с цикъл. Ако първото число е 0, изведете Няма данни. 1
#б) (6 т.) Изведете най-малкото число в редицата. 1
#в) (7 т.) Изведете колко пъти едно число е по-голямо от непосредствено предишното (брой нараствания). 1
#г) (6 т.) Изведете какъв процент от числата са отрицателни, закръглен до цяло число. 1

n = 1
a=[]
numbers = 0

while n!=0:
    n = int(input())
    if n != 0:
        a.append(n)
        numbers+=1

lowest = a[0]
otricatelno = 0
narstvaniq = 0

if a[0]==0:
    print("No data.")
    

for i in range(0,numbers):
    if a[i]<0:
        otricatelno+=1
    if a[i]<lowest:
        lowest = a[i]

for i in range(0,numbers-1):
    if a[i]<a[i+1]:
        narstvaniq+=1

otrProcent = otricatelno/numbers*100
print("Lowest:",lowest, "Narasvaniq: " ,narstvaniq, "Negative(%): ",otrProcent)