#Дано трехзначное число. Проверить истинность высказывания: «Цифры данного
#числа образуют возрастающую или убывающую последовательность».
def check_sequence(number):
    try:
        # Убедимся, что число трехзначное
        if 100 <= number <= 999:
            # Извлекаем цифры
            hundreds = number // 100
            tens = (number // 10) % 10
            units = number % 10
            # Проверяем на возрастающую и убывающую последовательность
            is_increasing = hundreds < tens < units
            is_decreasing = hundreds > tens > units

            return is_increasing or is_decreasing
        else:
            return False  # Не трехзначное число
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False
# Пример использования
try:
    number = int(input("Введите трехзначное число: "))
    if check_sequence(number):
        print("Цифры образуют возрастающую или убывающую последовательность.")
    else:
        print("Цифры не образуют возрастающую или убывающую последовательность.")
except ValueError:
    print("Пожалуйста, введите корректное целое число.")