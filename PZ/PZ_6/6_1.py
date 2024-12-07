#Дан целочисленный список размера N, не содержащий одинаковых чисел.
#Проверить, образуют ли его элементы арифметическую прогрессию. Если образуют,
#то вывести разность прогрессии, если нет — вывести 0.
def is_arithmetic_progression(lst):
    if len(lst) < 2:
        return 0  # Список слишком короткий для прогрессии

    diff = lst[1] - lst[0]

    for i in range(2, len(lst)):
        if lst[i] - lst[i - 1] != diff:
            return 0

    return diff


def main():
    try:
        N = int(input("Введите размер списка N: "))
        if N < 2:
            raise ValueError("Размер списка должен быть больше 1")

        lst = []
        for _ in range(N):
            num = int(input("Введите элемент списка: "))
            lst.append(num)

        result = is_arithmetic_progression(lst)
        print(result)
    except ValueError as e:
        print("Ошибка:", e)


# Запуск основной функции
main()