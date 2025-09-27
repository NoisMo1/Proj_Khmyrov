#Дано множество А из N точек (точки заданы своими координатами х, у).
#Среди всех точек этого множества,
#лежащих во второй четверти, найти точку, наиболее удаленную от начала координат.
#Если таких точек нет, то вывести точку с нулевыми координатами.
n = int(input("Введите количество точек N: "))

tochki = []
for i in range(n):
    x = int(input())
    y = int(input())
    tochki.append((x, y))

naydena = False
max_rasstoyanie = -1
luchshaya_tochka = (0, 0)

for (x, y) in tochki:
    if x < 0 and y > 0:
        naydena = True
        rasstoyanie = x * x + y * y
        if rasstoyanie > max_rasstoyanie:
            max_rasstoyanie = rasstoyanie
            luchshaya_tochka = (x, y)

if not naydena:
    luchshaya_tochka = (0, 0)

print(luchshaya_tochka[0])
print(luchshaya_tochka[1])
