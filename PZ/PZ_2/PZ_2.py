#Запрос ввода целого числа больше 999
a = (input("Введите число больше 999: "))
while type(a) != int: # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число больше 999: ")
print('Разряд 1000 =', a//1000%10) #Делим число a на 1000 с округлением вниз, затем берем остаток от деления на 10