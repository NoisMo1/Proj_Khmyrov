#Дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими). 
#Найти длину самого длинного слова.
def find_longest_word_length(text):
    words = text.split()
    if not words:
        return 0
    longest_length = max(len(word) for word in words)
    return longest_length

text = "Дана строка состоящая из русских слов разделенных пробелами"
result = find_longest_word_length(text)
print(f"Длина самого длинного слова: {result}")
