#Дано целое число. Если оно является положительным, то прибавить к нему 1; в
#противном случае вычесть из него 2. Вывести полученное число.
while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Ошибка ввода. Попробуйте еще раз.")

if number > 0:
    result = number + 1
elif number <= 0:
    result = number - 2
print(result)