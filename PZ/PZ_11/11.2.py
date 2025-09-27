#Из предложенного текстового файла (text18-22.txt) вывеси на экран его содержимое,
#количество букв в верхнем регистре.
#Сформировать новый файл,
#в который поместить текст в стихотворной форме предварительно заменив символы третей строки их числовыми кодами.


# Чтение исходного файла
with open("text18-22.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Вывод содержимого и подсчёт заглавных букв
uppercase_count = sum(1 for line in lines for char in line if char.isupper())
print("Содержимое файла:")
print("".join(lines))
print(f"Количество букв в верхнем регистре: {uppercase_count}")

# Обработка третей строки (если она существует)
if len(lines) >= 3:
    third_line = lines[2].strip()  # Убираем лишние пробелы и переносы
    encoded_line = " ".join(str(ord(char)) for char in third_line) + "\n"
    lines[2] = encoded_line

# Запись в новый файл
with open("encoded_poem.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)


print("Третья строка заменена на ASCII-коды. Результат сохранён в encoded_poem.txt.")
