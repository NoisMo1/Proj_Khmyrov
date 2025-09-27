
# Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1). -> Вариант 17
# https://bramus.github.io/ws1-sws-course-materials/assets/03/testform.jpg

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Testform")
root.geometry("600x400")
root.resizable(False, False)

header = tk.Label(root, text="Testform", font=("Arial", 16, "bold"))
header.grid(row=0, column=0, columnspan=2, sticky='w', padx=10, pady=10)

tk.Label(root, text="Name").grid(row=1, column=0, sticky='e', padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password").grid(row=2, column=0, sticky='e', padx=10, pady=5)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Gender").grid(row=3, column=0, sticky='e', padx=10, pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky='w', padx=10)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=4, column=1, sticky='w', padx=10)

tk.Label(root, text="Continent").grid(row=5, column=0, sticky='e', padx=10, pady=5)
continent_combo = ttk.Combobox(root, values=["Please select...", "Asia", "Europe", "North America", "South America", "Africa", "Australia", "Antarctica"])
continent_combo.current(0)
continent_combo.grid(row=5, column=1, padx=10, pady=5, sticky='w')

tk.Label(root, text="Meals").grid(row=6, column=0, sticky='ne', padx=10, pady=5)
meal_frame = tk.Frame(root)
meal_frame.grid(row=6, column=1, sticky='w', padx=10)
meal_vars = {
    "breakfast": tk.BooleanVar(),
    "lunch": tk.BooleanVar(),
    "dinner": tk.BooleanVar()
}
tk.Checkbutton(meal_frame, text="breakfast", variable=meal_vars["breakfast"]).pack(anchor='w')
tk.Checkbutton(meal_frame, text="lunch", variable=meal_vars["lunch"]).pack(anchor='w')
tk.Checkbutton(meal_frame, text="dinner", variable=meal_vars["dinner"]).pack(anchor='w')

tk.Label(root, text="Remark").grid(row=7, column=0, sticky='ne', padx=10, pady=5)
text_remark = tk.Text(root, height=5, width=40)
text_remark.grid(row=7, column=1, padx=10, pady=5)

btn_frame = tk.Frame(root)
btn_frame.grid(row=8, column=1, sticky='e', padx=10, pady=10)
tk.Button(btn_frame, text="Send", width=10).pack(side='left', padx=5)
tk.Button(btn_frame, text="Cancel", width=10, command=root.quit).pack(side='left', padx=5)

root.mainloop()
