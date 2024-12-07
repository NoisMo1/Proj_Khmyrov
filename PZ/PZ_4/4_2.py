#Дано целое число N (>0). Найти наибольшее целое число K, квадрат которого не
#превосходит N: K^2 < N. Функцию извлечения квадратного корня не использовать.
def find_max_k(N):
    low, high = 0, N
    while low <= high:
        mid = (low + high) // 2
        if mid * mid < N:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1


def main():
    try:
        N = int(input("Введите положительное целое число N: "))
        if N <= 0:
            raise ValueError("Число должно быть положительным")

        max_k = find_max_k(N)
        print(f"Наибольшее целое число K, такое что K^2 < {N}: {max_k}")
    except ValueError as e:
        print("Ошибка:", e)


# Запуск основной функции
main()