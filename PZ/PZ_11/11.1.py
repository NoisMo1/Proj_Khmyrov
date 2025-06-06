import os

# Проверяем, существует ли файл
if not os.path.exists("text18-22.txt"):
    print("Ошибка: Файл 'text18-22.txt' не найден.")
    print("Создайте файл вручную или автоматически? (1/2)")
    choice = input("Выберите 1 или 2: ")

    if choice == "1":
        print("Создайте файл 'text18-22.txt' вручную и запустите программу снова.")
        exit()
    elif choice == "2":
        # Автоматически создаем пример файла
        with open("text18-22.txt", "w", encoding="utf-8") as f:
            f.write("Я помню чудное мгновенье,\n")
            f.write("Передо мной явилась ты,\n")
            f.write("Как мимолётное виденье,\n")
            f.write("Как гений чистой красоты.\n")
        print("Файл 'text18-22.txt' создан автоматически.")
    else:
        print("Неверный выбор. Программа завершена.")
        exit()

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