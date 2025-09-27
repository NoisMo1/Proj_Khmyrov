# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9. -> ПЗ №2

import tkinter as tk
from tkinter import messagebox

def calculate_hours():
    try:
        seconds = int(entry_seconds.get())
        hours = seconds // 3600
        result_label.config(text=f"Кол-во полных часов: {hours}")
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Вы ввели не численный формат данных.")

root = tk.Tk()
root.title("Подсчёт часов с начала суток")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Введите кол-во секунд с начала суток:").pack(pady=10)
entry_seconds = tk.Entry(root, width=30)
entry_seconds.pack()

tk.Button(root, text="Вычислить", command=calculate_hours).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
