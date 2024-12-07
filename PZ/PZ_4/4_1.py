#Даны целые положительные числа N и K. Найти сумму 1^K + 2^К + ... + N^K
def sum_of_powers(N, K):
    total_sum = 0
    for i in range(1, N + 1):
        total_sum += i ** K
    return total_sum

def main():
    try:
        N = int(input("Введите положительное целое число N: "))
        K = int(input("Введите положительное целое число K: "))

        if N <= 0 or K <= 0:
            raise ValueError("Числа должны быть положительными")

        result = sum_of_powers(N, K)
        print(f"Сумма 1^{K} + 2^{K} + ... + {N}^{K} равна {result}")
    except ValueError as e:
        print("Ошибка:", e)

# Запуск основной функции
main()