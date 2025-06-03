# 1.Даны текущие оценки студента по дисциплине «Основы программирования» за
# месяц. Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и
# определить итоговую оценку за месяц.

grades = [5, 4, 3, 5, 2, 4, 5, 3, 4, 5]  # Пример списка оценок

count_2 = grades.count(2)
count_3 = grades.count(3)
count_4 = grades.count(4)
count_5 = grades.count(5)

print(f"Количество '2': {count_2}")
print(f"Количество '3': {count_3}")
print(f"Количество '4': {count_4}")
print(f"Количество '5': {count_5}")

average_grade = sum(grades) / len(grades)
final_grade = round(average_grade)  # Округляем среднее значение

print(f"Итоговая оценка: {final_grade}")