# Приложение УЧЕТ ВНУТРИОФИСНЫХ РАСХОДОВ для некоторой
# организации. БД должна содержать таблицу Канцелярия со следующей структурой
# записи: ФИО работника, отдел, вид расхода, сумма

import sqlite3
from datetime import datetime


class OfficeExpensesDB:
    def __init__(self, db_name="office_expenses.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Канцелярия (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                фио_работника TEXT NOT NULL,
                отдел TEXT NOT NULL,
                вид_расхода TEXT NOT NULL,
                сумма REAL NOT NULL,
                дата_расхода DATE DEFAULT CURRENT_DATE
            )
        ''')

        conn.commit()
        conn.close()

    def add_sample_data(self):

        sample_data = [
            ("Иванов Иван Иванович", "Бухгалтерия", "Бумага А4", 1500.50),
            ("Петрова Анна Сергеевна", "IT-отдел", "Картридж для принтера", 3200.00),
            ("Сидоров Михаил Петрович", "Отдел кадров", "Ручки шариковые", 450.75),
            ("Козлова Елена Викторовна", "Маркетинг", "Блокноты", 890.25),
            ("Федоров Алексей Дмитриевич", "Бухгалтерия", "Калькуляторы", 2100.00),
            ("Николаева Ольга Игоревна", "IT-отдел", "USB-флешки", 1750.30),
            ("Волков Денис Александрович", "Производство", "Папки-скоросшиватели", 680.90),
            ("Семенова Татьяна Владимировна", "Маркетинг", "Брендированные ручки", 1250.40),
            ("Кузнецов Артем Олегович", "Отдел кадров", "Бланки документов", 950.60),
            ("Абрамова Юлия Романовна", "Производство", "Ежедневники", 1100.75)
        ]

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        for data in sample_data:
            cursor.execute('''
                INSERT INTO Канцелярия (фио_работника, отдел, вид_расхода, сумма)
                VALUES (?, ?, ?, ?)
            ''', data)

        conn.commit()
        conn.close()
        print("Добавлено 10 тестовых записей")

    def add_expense(self):
        """Добавление новой записи о расходе"""
        print("\n=== ДОБАВЛЕНИЕ НОВОГО РАСХОДА ===")
        фио = input("ФИО работника: ")
        отдел = input("Отдел: ")
        вид_расхода = input("Вид расхода: ")
        сумма = float(input("Сумма: "))

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Канцелярия (фио_работника, отдел, вид_расхода, сумма)
            VALUES (?, ?, ?, ?)
        ''', (фио, отдел, вид_расхода, сумма))

        conn.commit()
        conn.close()
        print("Запись успешно добавлена!")

    def search_expenses(self):
        """Поиск записей с использованием WHERE"""
        print("\n=== ПОИСК РАСХОДОВ ===")
        print("1. Поиск по отделу")
        print("2. Поиск по ФИО работника")
        print("3. Поиск по виду расхода")
        print("4. Поиск расходов выше определенной суммы")
        print("5. Поиск расходов по диапазону сумм")
        print("6. Поиск по отделу и виду расхода")

        choice = input("Выберите тип поиска (1-6): ")

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        if choice == "1":
            # WHERE по отделу
            отдел = input("Введите отдел для поиска: ")
            cursor.execute('''
                SELECT * FROM Канцелярия 
                WHERE отдел = ? 
                ORDER BY сумма DESC
            ''', (отдел,))

        elif choice == "2":
            # WHERE по ФИО (частичное совпадение)
            фио = input("Введите ФИО или часть ФИО: ")
            cursor.execute('''
                SELECT * FROM Канцелярия 
                WHERE фио_работника LIKE ? 
                ORDER BY дата_расхода DESC
            ''', (f'%{фио}%',))

        elif choice == "3":
            # WHERE по виду расхода
            вид = input("Введите вид расхода: ")
            cursor.execute('''
                SELECT * FROM Канцелярия 
                WHERE вид_расхода LIKE ? 
                ORDER BY сумма DESC
            ''', (f'%{вид}%',))

        elif choice == "4":
            # WHERE с сравнением (сумма больше)
            min_сумма = float(input("Введите минимальную сумму: "))
            cursor.execute('''
                SELECT * FROM Канцелярия 
                WHERE сумма > ? 
                ORDER BY сумма DESC
            ''', (min_сумма,))

        elif choice == "5":
            # WHERE с диапазоном
            min_сумма = float(input("Минимальная сумма: "))
            max_сумма = float(input("Максимальная сумма: "))
            cursor.execute('''
                SELECT * FROM Канцелярия 
                WHERE сумма BETWEEN ? AND ? 
                ORDER BY сумма
            ''', (min_сумма, max_сумма))

        elif choice == "6":
            # WHERE с несколькими условиями
            отдел = input("Отдел: ")
            вид = input("Вид расхода: ")
            cursor.execute('''
                SELECT * FROM Канцелярия 
                WHERE отдел = ? AND вид_расхода LIKE ?
            ''', (отдел, f'%{вид}%'))

        else:
            print("Неверный выбор")
            conn.close()
            return

        results = cursor.fetchall()
        self.display_results(results)
        conn.close()

    def delete_expenses(self):
        """Удаление записей с использованием WHERE"""
        print("\n=== УДАЛЕНИЕ РАСХОДОВ ===")
        print("1. Удаление по ID записи")
        print("2. Удаление по ФИО работника")
        print("3. Удаление по отделу")
        print("4. Удаление расходов ниже определенной суммы")
        print("5. Удаление по виду расхода")
        print("6. Удаление старых записей (по дате)")

        choice = input("Выберите тип удаления (1-6): ")

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        if choice == "1":
            # DELETE с WHERE по ID
            record_id = int(input("Введите ID записи для удаления: "))
            cursor.execute('SELECT * FROM Канцелярия WHERE id = ?', (record_id,))
            record = cursor.fetchone()

            if record:
                print(f"Найдена запись: {record}")
                confirm = input("Удалить эту запись? (да/нет): ")
                if confirm.lower() == 'да':
                    cursor.execute('DELETE FROM Канцелярия WHERE id = ?', (record_id,))
                    print("Запись удалена")
            else:
                print("Запись не найдена")

        elif choice == "2":
            # DELETE с WHERE по ФИО
            фио = input("Введите ФИО работника для удаления его расходов: ")
            cursor.execute('SELECT COUNT(*) FROM Канцелярия WHERE фио_работника = ?', (фио,))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Найдено {count} записей для {фио}")
                confirm = input("Удалить все эти записи? (да/нет): ")
                if confirm.lower() == 'да':
                    cursor.execute('DELETE FROM Канцелярия WHERE фио_работника = ?', (фио,))
                    print(f"Удалено {count} записей")
            else:
                print("Записи не найдены")

        elif choice == "3":
            # DELETE с WHERE по отделу
            отдел = input("Введите отдел для удаления всех расходов: ")
            cursor.execute('SELECT COUNT(*) FROM Канцелярия WHERE отдел = ?', (отдел,))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Найдено {count} записей для отдела {отдел}")
                confirm = input("Удалить все эти записи? (да/нет): ")
                if confirm.lower() == 'да':
                    cursor.execute('DELETE FROM Канцелярия WHERE отдел = ?', (отдел,))
                    print(f"Удалено {count} записей")
            else:
                print("Записи не найдены")

        elif choice == "4":
            # DELETE с WHERE по сумме (меньше указанной)
            max_сумма = float(input("Удалить расходы с суммой меньше: "))
            cursor.execute('SELECT COUNT(*) FROM Канцелярия WHERE сумма < ?', (max_сумма,))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Найдено {count} записей с суммой меньше {max_сумма}")
                confirm = input("Удалить эти записи? (да/нет): ")
                if confirm.lower() == 'да':
                    cursor.execute('DELETE FROM Канцелярия WHERE сумма < ?', (max_сумма,))
                    print(f"Удалено {count} записей")
            else:
                print("Записи не найдены")

        elif choice == "5":
            # DELETE с WHERE по виду расхода
            вид = input("Введите вид расхода для удаления: ")
            cursor.execute('SELECT COUNT(*) FROM Канцелярия WHERE вид_расхода LIKE ?', (f'%{вид}%',))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Найдено {count} записей с видом расхода '{вид}'")
                confirm = input("Удалить эти записи? (да/нет): ")
                if confirm.lower() == 'да':
                    cursor.execute('DELETE FROM Канцелярия WHERE вид_расхода LIKE ?', (f'%{вид}%',))
                    print(f"Удалено {count} записей")
            else:
                print("Записи не найдены")

        elif choice == "6":
            # DELETE с WHERE по дате
            дата = input("Удалить записи старше (гггг-мм-дд): ")
            cursor.execute('SELECT COUNT(*) FROM Канцелярия WHERE дата_расхода < ?', (дата,))
            count = cursor.fetchone()[0]

            if count > 0:
                print(f"Найдено {count} записей старше {дата}")
                confirm = input("Удалить эти записи? (да/нет): ")
                if confirm.lower() == 'да':
                    cursor.execute('DELETE FROM Канцелярия WHERE дата_расхода < ?', (дата,))
                    print(f"Удалено {count} записей")
            else:
                print("Записи не найдены")

        else:
            print("Неверный выбор")

        conn.commit()
        conn.close()

    def update_expenses(self):
        """Редактирование записей с использованием WHERE"""
        print("\n=== РЕДАКТИРОВАНИЕ РАСХОДОВ ===")
        print("1. Редактирование суммы по ID")
        print("2. Редактирование отдела для конкретного работника")
        print("3. Обновление вида расхода по отделу")
        print("4. Увеличение суммы на процент для отдела")
        print("5. Обновление ФИО работника")
        print("6. Корректировка сумм (умножение на коэффициент)")

        choice = input("Выберите тип редактирования (1-6): ")

        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        if choice == "1":
            # UPDATE с WHERE по ID
            record_id = int(input("Введите ID записи: "))
            новая_сумма = float(input("Новая сумма: "))

            cursor.execute('''
                UPDATE Канцелярия 
                SET сумма = ? 
                WHERE id = ?
            ''', (новая_сумма, record_id))
            print("Запись обновлена")

        elif choice == "2":
            # UPDATE с WHERE по ФИО
            фио = input("Введите ФИО работника: ")
            новый_отдел = input("Новый отдел: ")

            cursor.execute('''
                UPDATE Канцелярия 
                SET отдел = ? 
                WHERE фио_работника = ?
            ''', (новый_отдел, фио))
            print("Записи обновлены")

        elif choice == "3":
            # UPDATE с WHERE по отделу
            отдел = input("Введите отдел: ")
            новый_вид = input("Новый вид расхода: ")

            cursor.execute('''
                UPDATE Канцелярия 
                SET вид_расхода = ? 
                WHERE отдел = ?
            ''', (новый_вид, отдел))
            print("Записи обновлены")

        elif choice == "4":
            # UPDATE с вычислением
            отдел = input("Введите отдел: ")
            процент = float(input("На сколько процентов увеличить сумму: "))
            коэффициент = 1 + процент / 100

            cursor.execute('''
                UPDATE Канцелярия 
                SET сумма = сумма * ? 
                WHERE отдел = ?
            ''', (коэффициент, отдел))
            print("Суммы обновлены")

        elif choice == "5":
            # UPDATE с WHERE по старому ФИО
            старое_фио = input("Старое ФИО: ")
            новое_фио = input("Новое ФИО: ")

            cursor.execute('''
                UPDATE Канцелярия 
                SET фио_работника = ? 
                WHERE фио_работника = ?
            ''', (новое_фио, старое_фио))
            print("ФИО обновлено")

        elif choice == "6":
            # UPDATE с WHERE по диапазону сумм
            min_сумма = float(input("Минимальная сумма: "))
            max_сумма = float(input("Максимальная сумма: "))
            коэффициент = float(input("Коэффициент умножения: "))

            cursor.execute('''
                UPDATE Канцелярия 
                SET сумма = сумма * ? 
                WHERE сумма BETWEEN ? AND ?
            ''', (коэффициент, min_сумма, max_сумма))
            print("Суммы скорректированы")

        else:
            print("Неверный выбор")

        conn.commit()
        conn.close()

    def display_all_expenses(self):
        """Отображение всех записей"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM Канцелярия 
            ORDER BY дата_расхода DESC, id DESC
        ''')

        results = cursor.fetchall()
        self.display_results(results)
        conn.close()

    def display_results(self, results):
        """Отображение результатов запроса"""
        if not results:
            print("Записи не найдены")
            return

        print(f"\nНайдено записей: {len(results)}")
        print("-" * 100)
        print(f"{'ID':<3} {'ФИО работника':<25} {'Отдел':<15} {'Вид расхода':<20} {'Сумма':<10} {'Дата':<10}")
        print("-" * 100)

        total = 0
        for row in results:
            print(f"{row[0]:<3} {row[1]:<25} {row[2]:<15} {row[3]:<20} {row[4]:<10} {row[5]:<10}")
            total += row[4]

        print("-" * 100)
        print(f"{'ИТОГО:':<65} {total:<10.2f}")

    def get_statistics(self):
        """Получение статистики по расходам"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        print("\n=== СТАТИСТИКА РАСХОДОВ ===")

        # Общая сумма расходов
        cursor.execute('SELECT SUM(сумма) FROM Канцелярия')
        total = cursor.fetchone()[0]
        print(f"Общая сумма расходов: {total:.2f} руб.")

        # Сумма по отделам
        cursor.execute('''
            SELECT отдел, SUM(сумма) 
            FROM Канцелярия 
            GROUP BY отдел 
            ORDER BY SUM(сумма) DESC
        ''')
        print("\nРасходы по отделам:")
        for отдел, сумма in cursor.fetchall():
            print(f"  {отдел}: {сумма:.2f} руб.")

        # Самые частые виды расходов
        cursor.execute('''
            SELECT вид_расхода, COUNT(*), SUM(сумма)
            FROM Канцелярия 
            GROUP BY вид_расхода 
            ORDER BY COUNT(*) DESC 
            LIMIT 5
        ''')
        print("\nСамые частые виды расходов:")
        for вид, колво, сумма in cursor.fetchall():
            print(f"  {вид}: {колво} раз, {сумма:.2f} руб.")

        conn.close()


def main():
    db = OfficeExpensesDB()

    # Добавляем тестовые данные если таблица пустая
    conn = sqlite3.connect(db.db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Канцелярия')
    count = cursor.fetchone()[0]
    conn.close()

    if count == 0:
        db.add_sample_data()

    while True:
        print("\n=== УЧЕТ ВНУТРИОФИСНЫХ РАСХОДОВ ===")
        print("1. Показать все расходы")
        print("2. Добавить новый расход")
        print("3. Поиск расходов")
        print("4. Удаление расходов")
        print("5. Редактирование расходов")
        print("6. Статистика расходов")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            db.display_all_expenses()
        elif choice == "2":
            db.add_expense()
        elif choice == "3":
            db.search_expenses()
        elif choice == "4":
            db.delete_expenses()
        elif choice == "5":
            db.update_expenses()
        elif choice == "6":
            db.get_statistics()
        elif choice == "7":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор, попробуйте снова")


if __name__ == "__main__":
    main()