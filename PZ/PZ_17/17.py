import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Переменная для хранения текущего выражения
        self.expression = ""
        self.input_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        """Создание виджетов калькулятора"""
        # Поле ввода
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=20, padx=20, fill=tk.X)
        
        input_entry = tk.Entry(
            input_frame, 
            textvariable=self.input_var,
            font=('Arial', 18),
            justify='right',
            state='readonly'
        )
        input_entry.pack(fill=tk.X, ipady=10)
        
        # Клавиши калькулятора
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Расположение кнопок
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', 'CE', '←']
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=('Arial', 14),
                    command=lambda t=text: self.button_click(t),
                    height=2,
                    width=5
                )
                btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
                
                # Особые стили для разных кнопок
                if text in ['=', 'C', 'CE', '←']:
                    btn.configure(bg='#ff9900', fg='white')
                elif text in ['/', '*', '-', '+']:
                    btn.configure(bg='#666666', fg='white')
                else:
                    btn.configure(bg='#e0e0e0')
        
        # Настройка веса строк и столбцов
        for i in range(len(buttons)):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(len(buttons[0])):
            buttons_frame.columnconfigure(j, weight=1)
    
    def button_click(self, text):
        """Обработка нажатия кнопок"""
        try:
            if text == '=':
                # Вычисление результата
                result = str(eval(self.expression))
                self.input_var.set(result)
                self.expression = result
            elif text == 'C':
                # Очистка всего
                self.expression = ""
                self.input_var.set("")
            elif text == 'CE':
                # Очистка последнего элемента
                if self.expression:
                    self.expression = self.expression[:-1]
                    self.input_var.set(self.expression)
            elif text == '←':
                # Удаление последнего символа
                if self.expression:
                    self.expression = self.expression[:-1]
                    self.input_var.set(self.expression)
            else:
                # Добавление символа к выражению
                self.expression += str(text)
                self.input_var.set(self.expression)
                
        except Exception as e:
            messagebox.showerror("Ошибка", "Некорректное выражение!")
            self.expression = ""
            self.input_var.set("")

def run_calculator():
    """Запуск калькулятора"""
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

# Если нужно запускать отдельно
if __name__ == "__main__":
    run_calculator()
