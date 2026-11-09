#Две прости числа са близнаци, ако разликата между тях е 2. Например 11 и 13.
#а) (5 т.) Въвежда се цяло число n. Докато n < 5, програмата чете ново число.
#б) (8 т.) Напишете проверка дали дадено число е просто. Делителите трябва да се проверяват само до корен квадратен от числото.
# Не се разрешава използване на готови библиотеки.
#в) (7 т.) Изведете всички двойки близнаци (p, p + 2), за които p + 2 ≤ n, по една двойка на ред.
#г) (5 т.) Изведете броя на двойките и най-голямата двойка.

def squareRoot(i):
    k = int(i**0.5)
    prost=1
    for j in range(1,k):
        if i%j==0:
            prost=0
    return prost

n=0
while n<5:
    n = int(input("Input n: "))

p=1
naigolqm = 0
bliznaci = 0

while p+2<=n:
    a=squareRoot(p)
    j=p+2
    b=squareRoot(j)
    if a==1 and b==1:
        print(p, p+2)
        bliznaci+=1
        naigolqm=p+2
    p+=1
    
print("Dvoiki:", bliznaci)
print("Nai golqma", naigolqm-2, naigolqm)