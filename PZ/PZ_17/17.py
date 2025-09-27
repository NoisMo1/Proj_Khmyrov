import tkinter as tk
from tkinter import ttk, messagebox
import os


class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Регистрационная форма")
        self.root.geometry("500x600")
        self.root.configure(bg='#f0f0f0')

        # Создание основного фрейма
        main_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Заголовок
        title_label = tk.Label(
            main_frame,
            text="Регистрация",
            font=('Arial', 24, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=(0, 20))

        # Фрейм для формы
        form_frame = tk.Frame(main_frame, bg='#f0f0f0')
        form_frame.pack(fill=tk.BOTH, expand=True)

        # Поля формы
        self.create_form_field(form_frame, "Имя:", 0)
        self.create_form_field(form_frame, "Фамилия:", 1)
        self.create_form_field(form_frame, "Email:", 2)
        self.create_form_field(form_frame, "Телефон:", 3)
        self.create_form_field(form_frame, "Пароль:", 4, show="*")
        self.create_form_field(form_frame, "Подтверждение пароля:", 5, show="*")

        # Выбор страны
        country_frame = tk.Frame(form_frame, bg='#f0f0f0')
        country_frame.grid(row=6, column=0, columnspan=2, sticky='ew', pady=10)

        tk.Label(
            country_frame,
            text="Страна:",
            font=('Arial', 12),
            bg='#f0f0f0',
            anchor='w'
        ).pack(side=tk.LEFT, padx=(0, 10))

        self.country_var = tk.StringVar()
        countries = ['Россия', 'США', 'Германия', 'Франция', 'Великобритания', 'Япония']
        country_combo = ttk.Combobox(
            country_frame,
            textvariable=self.country_var,
            values=countries,
            state='readonly',
            width=38
        )
        country_combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        country_combo.set('Россия')

        # Чекбоксы
        checkbox_frame = tk.Frame(form_frame, bg='#f0f0f0')
        checkbox_frame.grid(row=7, column=0, columnspan=2, sticky='w', pady=10)

        self.terms_var = tk.BooleanVar()
        terms_check = tk.Checkbutton(
            checkbox_frame,
            text="Я принимаю условия пользовательского соглашения",
            variable=self.terms_var,
            bg='#f0f0f0',
            font=('Arial', 10)
        )
        terms_check.pack(anchor='w')

        self.newsletter_var = tk.BooleanVar(value=True)
        newsletter_check = tk.Checkbutton(
            checkbox_frame,
            text="Подписаться на рассылку новостей",
            variable=self.newsletter_var,
            bg='#f0f0f0',
            font=('Arial', 10)
        )
        newsletter_check.pack(anchor='w', pady=(5, 0))

        # Кнопки
        button_frame = tk.Frame(form_frame, bg='#f0f0f0')
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)

        register_btn = tk.Button(
            button_frame,
            text="Зарегистрироваться",
            command=self.register,
            bg='#4CAF50',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        register_btn.pack(side=tk.LEFT, padx=(0, 10))

        clear_btn = tk.Button(
            button_frame,
            text="Очистить",
            command=self.clear_form,
            bg='#f44336',
            fg='white',
            font=('Arial', 12),
            padx=20,
            pady=10,
            cursor='hand2'
        )
        clear_btn.pack(side=tk.LEFT)

        # Хранение полей ввода
        self.entries = {}

    def create_form_field(self, parent, label_text, row):
        """Создание поля формы с меткой"""
        label = tk.Label(
            parent,
            text=label_text,
            font=('Arial', 12),
            bg='#f0f0f0',
            anchor='w'
        )
        label.grid(row=row, column=0, sticky='w', pady=5)

        show_char = "" if "show" not in locals() else "*"
        entry = tk.Entry(
            parent,
            font=('Arial', 12),
            width=30,
            show=show_char
        )
        entry.grid(row=row, column=1, sticky='ew', pady=5, padx=(10, 0))

        # Сохраняем ссылку на поле ввода
        field_name = label_text.replace(':', '').lower()
        self.entries[field_name] = entry

        # Настройка веса колонок для растягивания
        parent.columnconfigure(1, weight=1)

    def register(self):
        """Обработка регистрации"""
        try:
            # Получение данных из полей
            data = {}
            for field_name, entry in self.entries.items():
                data[field_name] = entry.get().strip()

            # Проверка обязательных полей
            if not all([data['имя'], data['фамилия'], data['email'], data['пароль']]):
                messagebox.showerror("Ошибка", "Заполните все обязательные поля!")
                return

            # Проверка пароля
            if data['пароль'] != data['подтверждение пароля']:
                messagebox.showerror("Ошибка", "Пароли не совпадают!")
                return

            # Проверка согласия с условиями
            if not self.terms_var.get():
                messagebox.showerror("Ошибка", "Необходимо принять условия пользовательского соглашения!")
                return

            # Проверка email
            if '@' not in data['email']:
                messagebox.showerror("Ошибка", "Введите корректный email!")
                return

            # Сообщение об успешной регистрации
            messagebox.showinfo(
                "Успешная регистрация",
                f"Регистрация прошла успешно!\n\n"
                f"Имя: {data['имя']}\n"
                f"Фамилия: {data['фамилия']}\n"
                f"Email: {data['email']}\n"
                f"Телефон: {data['телефон'] or 'Не указан'}\n"
                f"Страна: {self.country_var.get()}\n"
                f"Рассылка: {'Да' if self.newsletter_var.get() else 'Нет'}"
            )

            # Очистка формы после успешной регистрации
            self.clear_form()

        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

    def clear_form(self):
        """Очистка всех полей формы"""
        for entry in self.entries.values():
            entry.delete(0, tk.END)

        self.country_var.set('Россия')
        self.terms_var.set(False)
        self.newsletter_var.set(True)


def task_3_os_operations():
    """Задание 3: Работа с модулем OS"""
    print("\n=== ЗАДАНИЕ 3: РАБОТА С МОДУЛЕМ OS ===\n")

    # 1. Переход в каталог PZ11 и вывод списка файлов
    print("1. Файлы в каталоге PZ11 (без подкаталогов):")
    try:
        # Создаем тестовую структуру для демонстрации
        os.makedirs('PZ11', exist_ok=True)
        test_files = ['main.py', 'utils.py', 'report.pdf', 'data.txt']
        for file in test_files:
            with open(f'PZ11/{file}', 'w') as f:
                f.write('')

        # Выводим только файлы (не каталоги)
        files = [f for f in os.listdir('PZ11') if os.path.isfile(os.path.join('PZ11', f))]
        for file in files:
            print(f"   - {file}")
    except Exception as e:
        print(f"   Ошибка: {e}")

    # 2. Создание папок и работа с файлами
    print("\n2. Создание папок и перемещение файлов:")
    try:
        # Создаем структуру папок
        os.makedirs('test/test1', exist_ok=True)

        # Создаем тестовые файлы для P36 и P37
        os.makedirs('P36', exist_ok=True)
        os.makedirs('P37', exist_ok=True)

        with open('P36/file1.txt', 'w') as f:
            f.write('Файл 1 из P36')
        with open('P36/file2.txt', 'w') as f:
            f.write('Файл 2 из P36')
        with open('P37/original.txt', 'w') as f:
            f.write('Файл из P37')

        # Перемещаем файлы
        os.rename('P36/file1.txt', 'test/file1.txt')
        os.rename('P36/file2.txt', 'test/file2.txt')
        os.rename('P37/original.txt', 'test/test1/original.txt')

        # Переименовываем файл
        os.rename('test/test1/original.txt', 'test/test1/test.txt')

        # Выводим информацию о размерах файлов
        total_size = 0
        for file in os.listdir('test'):
            file_path = os.path.join('test', file)
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                total_size += size
                print(f"   {file}: {size} байт")

        print(f"   Общий размер файлов в папке test: {total_size} байт")

    except Exception as e:
        print(f"   Ошибка: {e}")

    # 3. Поиск файла с самым коротким именем в PZ11
    print("\n3. Файл с самым коротким именем в PZ11:")
    try:
        files = [f for f in os.listdir('PZ11') if os.path.isfile(os.path.join('PZ11', f))]
        if files:
            shortest_file = min(files, key=len)
            print(f"   {os.path.basename(shortest_file)}")
        else:
            print("   Файлы не найдены")
    except Exception as e:
        print(f"   Ошибка: {e}")

    # 4. Запуск PDF файла (если существует)
    print("\n4. Запуск PDF файла:")
    try:
        pdf_files = [f for f in os.listdir('PZ11') if f.endswith('.pdf')]
        if pdf_files:
            pdf_path = os.path.join('PZ11', pdf_files[0])
            print(f"   Запуск файла: {pdf_files[0]}")
            # Раскомментируйте следующую строку для реального запуска
            # os.startfile(pdf_path)
            print("   (Запуск отключен в демонстрационных целях)")
        else:
            print("   PDF файлы не найдены")
    except Exception as e:
        print(f"   Ошибка: {e}")

    # 5. Удаление файла test.txt
    print("\n5. Удаление файла test.txt:")
    try:
        if os.path.exists('test/test1/test.txt'):
            os.remove('test/test1/test.txt')
            print("   Файл test.txt удален")
        else:
            print("   Файл test.txt не найден")
    except Exception as e:
        print(f"   Ошибка: {e}")


def main():
    """Главная функция"""
    print("Практическое занятие №17")
    print("GUI Tkinter и модуль OS")
    print("=" * 40)

    # Запуск GUI приложения
    root = tk.Tk()
    app = RegistrationForm(root)

    # Запуск OS операций в консоли
    task_3_os_operations()

    root.mainloop()


if __name__ == "__main__":
    main()
