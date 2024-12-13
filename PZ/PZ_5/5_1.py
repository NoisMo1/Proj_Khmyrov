#С помощью функций получить вертикальную и горизонтальную линии. Линия
#проводится многократной печатью символа. Заключить слово в рамку из
#полученных линий
def horizontal_line(length, char='*'):
    return char * length


def vertical_lines(word, char='|'):
    lines = []
    for _ in word:
        lines.append(char)
    return '\n'.join(lines)


def frame_word(word):
    top_bottom = horizontal_line(len(word) + 2)
    sides = vertical_lines(word)

    framed_word = (
        f"{top_bottom}\n"
        f"{sides} {word} {sides}\n"
        f"{top_bottom}"
    )

    return framed_word


def main():
    try:
        word = input("Введите слово: ")
        if not word.isalpha():
            raise ValueError("Слово должно содержать только буквы")

        result = frame_word(word)
        print(result)
    except ValueError as e:
        print("Ошибка:", e)


# Запуск основной функции
main()