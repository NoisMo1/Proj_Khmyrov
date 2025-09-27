#Дан список размера N и целые числа К и L (1 < K L ≤ N).
#Найти среднее арифметическое всех элементов списка, 
#кроме элементов с номерами от к до включительно.
n = int(input("Введите размер списка N: "))
k = int(input("Введите K (начало исключаемого диапазона): "))
l = int(input("Введите L (конец исключаемого диапазона): "))

print("Введите", n, "целых чисел:")
spisok = []
for i in range(n):
    chislo = int(input())
    spisok.append(chislo)

novy_spisok = []
for i in range(n):
    if i + 1 < k or i + 1 > l:
        novy_spisok.append(spisok[i])

if len(novy_spisok) == 0:
    print("Нет элементов для вычисления среднего.")
else:
    srednee = sum(novy_spisok) / len(novy_spisok)
    print("Среднее арифметическое:", srednee)
    
