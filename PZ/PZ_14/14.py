# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
# маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле.

import os

# Проверяем текущую директорию
print("Текущая директория:", os.getcwd())

# Убедимся, что файл существует
file_path = r'C:\Proj_Khmyrov\PZ\PZ_14\ip_address.txt'  # Полный путь
if not os.path.exists(file_path):
    print(f"Файл {file_path} не найден! Проверьте путь.")
    exit()

# Основной код
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    zero_count = 0
    other_count = 0

    with open('zero_octet.txt', 'w') as zero_file, \
         open('other_octet.txt', 'w') as other_file:
        for line in lines:
            line = line.strip()
            if not line:
                continue
            octets = line.split('.')
            if len(octets) == 4 and octets[3] == '0':
                zero_file.write(line + '\n')
                zero_count += 1
            else:
                other_file.write(line + '\n')
                other_count += 1

    print(f"Строк с '.0': {zero_count}")
    print(f"Остальных строк: {other_count}")

except Exception as e:
    print("Ошибка:", e)