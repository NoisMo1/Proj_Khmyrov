def get_number():
    while True:
        try:
            number = int(input("Введите число больше 999: "))
            if number > 999:
                return number
            else:
                print("Число должно быть больше 999.")
        except ValueError:
            print("Неверный ввод! Пожалуйста, введите целое число.")

number = get_number()
thousands_digit = number // 1000 % 10
print(f'Разряд 1000 = {thousands_digit}')