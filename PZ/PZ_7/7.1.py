#Дана строка, изображающая целое положительное число. 
#Вывести сумму цифр этого числа.
number_str = input("Введите целое положительное число: ")
sum_of_digits = 0
for digit in number_str:
    sum_of_digits += int(digit)
print("Сумма цифр числа:", sum_of_digits)
