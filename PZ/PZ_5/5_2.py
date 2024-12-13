#Описать функцию TrianglePS(a, P, S), вычисляющую по стороне a равностороннего
# его периметр P = 3*a и площадь S = a2 √3/4 (a — входной, P и S —
#выходные параметры; все параметры являются вещественными). С помощью этой
#функции найти периметры и площади трех равносторонних треугольников с
#данными сторонами.
import math


def TrianglePS(a, P, S):
    P = 3 * a
    S = a ** 2 * math.sqrt(3) / 4
    return P, S


def main():
    try:
        triangles = [
            float(input("Введите сторону первого треугольника: ")),
            float(input("Введите сторону второго треугольника: ")),
            float(input("Введите сторону третьего треугольника: "))
        ]

        results = []
        for side in triangles:
            P, S = TrianglePS(side, None, None)
            results.append((side, P, S))

        for side, P, S in results:
            print(f"Сторона: {side:.2f}, Периметр: {P:.2f}, Площадь: {S:.2f}")
    except ValueError as e:
        print("Ошибка:", e)


# Запуск основной функции
main()