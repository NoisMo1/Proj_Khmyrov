#Дано трехзначное число. Проверить истинность высказывания: «Цифры данного
#числа образуют возрастающую или убывающую последовательность».
def is_sequence_increasing_or_decreasing(number):
    digits = str(number) #Преобразуем число в строку для удобства работы с отдельными цифрами
    if len(digits) != 3: #Проверяем, что длина числа равна трем
        return False
    increasing = digits[0] < digits[1] < digits[2] #Проверяем возрастание
    decreasing = digits[0] > digits[1] > digits[2] #Проверяем убывание
    return increasing or decreasing  #Возвращаем истину, если выполнено хотя бы одно условие
number = int(input("Введите трехзначное число: "))
if is_sequence_increasing_or_decreasing(number):
    print("Цифры числа образуют возрастающую или убывающую последовательность")
else:
    print("Цифры числа не образуют возрастающую или убывающую последовательность")