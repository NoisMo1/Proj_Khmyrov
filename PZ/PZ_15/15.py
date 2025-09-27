#Приложение УЧЕТ ВНУТРИОФИСНЫХ РАСХОДОВ для некоторой организации.
#БД должна содержать таблицу Канцелярия со следующей структурой записи:
#ФИО работника, отдел, вид расхода.

import sqlite3


def init_db(conn):
    """Создаёт таблицу, если её нет."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Канцелярия (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio TEXT NOT NULL,
            otdel TEXT NOT NULL,
            rashod TEXT NOT NULL
        )
    ''')
    conn.commit()


def add_sample_data(conn):
    """Добавляет 10 примеров записей."""
    data = [
        ("Иванов И.И.", "Бухгалтерия", "Бумага А4"),
        ("Петрова М.С.", "Кадры", "Ручки"),
        ("Сидоров А.П.", "IT", "Флешки"),
        ("Кузнецова Е.В.", "Бухгалтерия", "Конверты"),
        ("Морозов Д.С.", "IT", "Мышки"),
        ("Волкова А.И.", "Кадры", "Блокноты"),
        ("Новиков С.А.", "Бухгалтерия", "Скобы"),
        ("Зайцева О.Н.", "IT", "Клавиатуры"),
        ("Лебедев А.В.", "Кадры", "Маркеры"),
        ("Громова Т.П.", "Бухгалтерия", "Папки")
    ]
    conn.executemany(
        "INSERT INTO Канцелярия (fio, otdel, rashod) VALUES (?, ?, ?)",
        data
    )
    conn.commit()
    print("Добавлено 10 записей.")


def show_all(conn):
    """Выводит все записи."""
    cursor = conn.execute("SELECT * FROM Канцелярия")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"{row[0]}: {row[1]}, {row[2]}, {row[3]}")
    else:
        print("Таблица пуста.")


def search(conn):
    """Поиск по трём разным условиям."""
    print("1 — по ФИО, 2 — по отделу, 3 — по расходу")
    choice = input("Выберите тип поиска: ")
    query = None
    param = None

    if choice == "1":
        value = input("ФИО (можно часть): ")
        query = "SELECT * FROM Канцелярия WHERE fio LIKE ?"
        param = (f"%{value}%",)
    elif choice == "2":
        value = input("Отдел: ")
        query = "SELECT * FROM Канцелярия WHERE otdel = ?"
        param = (value,)
    elif choice == "3":
        value = input("Вид расхода: ")
        query = "SELECT * FROM Канцелярия WHERE rashod = ?"
        param = (value,)
    else:
        print("Неверный выбор.")
        return

    try:
        cursor = conn.execute(query, param)
        results = cursor.fetchall()
        if results:
            for r in results:
                print(f"{r[0]}: {r[1]}, {r[2]}, {r[3]}")
        else:
            print("Ничего не найдено.")
    except sqlite3.Error as e:
        print("Ошибка поиска:", e)


def delete(conn):
    """Удаление по трём условиям."""
    print("1 — по ID, 2 — по отделу, 3 — по расходу")
    choice = input("Выберите тип удаления: ")
    query = None
    param = None

    if choice == "1":
        value = input("ID: ")
        query = "DELETE FROM Канцелярия WHERE id = ?"
        param = (value,)
    elif choice == "2":
        value = input("Отдел: ")
        query = "DELETE FROM Канцелярия WHERE otdel = ?"
        param = (value,)
    elif choice == "3":
        value = input("Вид расхода: ")
        query = "DELETE FROM Канцелярия WHERE rashod = ?"
        param = (value,)
    else:
        print("Неверный выбор.")
        return

    try:
        conn.execute(query, param)
        conn.commit()
        print("Записи удалены.")
    except sqlite3.Error as e:
        print("Ошибка удаления:", e)


def update(conn):
    """Редактирование по трём условиям."""
    print("1 — изменить расход по ID")
    print("2 — изменить отдел по ФИО")
    print("3 — изменить ФИО по отделу и расходу")
    choice = input("Выберите действие: ")

    try:
        if choice == "1":
            id_val = input("ID: ")
            rashod = input("Новый расход: ")
            conn.execute("UPDATE Канцелярия SET rashod = ? WHERE id = ?", (rashod, id_val))
        elif choice == "2":
            fio = input("ФИО: ")
            otdel = input("Новый отдел: ")
            conn.execute("UPDATE Канцелярия SET otdel = ? WHERE fio = ?", (otdel, fio))
        elif choice == "3":
            otdel = input("Отдел: ")
            rashod = input("Расход: ")
            fio = input("Новое ФИО: ")
            conn.execute(
                "UPDATE Канцелярия SET fio = ? WHERE otdel = ? AND rashod = ?",
                (fio, otdel, rashod)
            )
        else:
            print("Неверный выбор.")
            return
        conn.commit()
        print("Запись(и) обновлены.")
    except sqlite3.Error as e:
        print("Ошибка обновления:", e)


def main():
    try:
        with sqlite3.connect("office.db") as conn:
            init_db(conn)

            while True:
                print("\n1 — показать всё")
                print("2 — добавить 10 записей")
                print("3 — поиск")
                print("4 — удаление")
                print("5 — редактирование")
                print("0 — выход")
                action = input("Выберите действие: ")

                if action == "1":
                    show_all(conn)
                elif action == "2":
                    add_sample_data(conn)
                elif action == "3":
                    search(conn)
                elif action == "4":
                    delete(conn)
                elif action == "5":
                    update(conn)
                elif action == "0":
                    break
                else:
                    print("Неверный ввод.")
    except sqlite3.Error as e:
        print("Ошибка базы данных:", e)
    except Exception as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
