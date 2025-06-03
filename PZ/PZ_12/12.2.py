# 2.Из заданной строки отобразить только символы пунктуации. Использовать
# библиотеку string.
# Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

import string

input_str = '--msg-template="$FileDir$\\{path}:{line}:{column}:{C}:({symbol}){msg}"'

punctuation_chars = []
for char in input_str:
    if char in string.punctuation:
        punctuation_chars.append(char)

result = ''.join(punctuation_chars)
print(result)