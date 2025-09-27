#Задание 3.
#Задание предполагает, что у студента есть проект с практическими работами (№№ 2-13),
#оформленный согласно требованиям.
#Все задания выполняются с использованием модуля OS:
import sqlite3

# Создаем базу данных и таблицу
def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            quantity INTEGER
        )
    ''')
    
    # Добавляем 10 тестовых товаров
    products = [
        (1, 'Яблоки', 50.0, 100),
        (2, 'Бананы', 70.0, 80),
        (3, 'Молоко', 60.0, 50),
        (4, 'Хлеб', 30.0, 40),
        (5, 'Сыр', 200.0, 30),
        (6, 'Кофе', 300.0, 20),
        (7, 'Чай', 150.0, 25),
        (8, 'Сахар', 40.0, 60),
        (9, 'Масло', 80.0, 35),
        (10, 'Яйца', 90.0, 45)
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO products VALUES (?, ?, ?, ?)', products)
    conn.commit()
    conn.close()
    print("База данных создана! Добавлено 10 товаров.")

# Показать все товары
def show_all():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    
    print("\nВсе товары:")
    for product in products:
        print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
    
    conn.close()

# Поиск товаров (3 разных способа)
def search_products():
    print("\n1. Поиск по названию")
    print("2. Поиск по цене (меньше указанной)")
    print("3. Поиск по количеству (больше указанного)")
    
    choice = input("Выберите способ поиска (1-3): ")
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    if choice == '1':
        # Поиск по названию
        name = input("Введите название товара: ")
        cursor.execute('SELECT * FROM products WHERE name LIKE ?', (f'%{name}%',))
    
    elif choice == '2':
        # Поиск по цене
        price = float(input("Введите максимальную цену: "))
        cursor.execute('SELECT * FROM products WHERE price < ?', (price,))
    
    elif choice == '3':
        # Поиск по количеству
        quantity = int(input("Введите минимальное количество: "))
        cursor.execute('SELECT * FROM products WHERE quantity > ?', (quantity,))
    
    else:
        print("Неверный выбор!")
        return
    
    results = cursor.fetchall()
    conn.close()
    
    if results:
        print("\nНайдены товары:")
        for product in results:
            print(f"ID: {product[0]}, Название: {product[1]}, Цена: {product[2]}, Количество: {product[3]}")
    else:
        print("Товары не найдены!")

# Удаление товаров (3 разных способа)
def delete_products():
    print("\n1. Удалить по ID")
    print("2. Удалить по названию")
    print("3. Удалить товары с количеством меньше указанного")
    
    choice = input("Выберите способ удаления (1-3): ")
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    if choice == '1':
        # Удаление по ID
        product_id = int(input("Введите ID товара: "))
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    
    elif choice == '2':
        # Удаление по названию
        name = input("Введите название товара: ")
        cursor.execute('DELETE FROM products WHERE name = ?', (name,))
    
    elif choice == '3':
        # Удаление по количеству
        quantity = int(input("Введите максимальное количество: "))
        cursor.execute('DELETE FROM products WHERE quantity < ?', (quantity,))
    
    else:
        print("Неверный выбор!")
        return
    
    conn.commit()
    print(f"Удалено товаров: {cursor.rowcount}")
    conn.close()

# Редактирование товаров (3 разных способа)
def edit_products():
    print("\n1. Изменить цену по ID")
    print("2. Изменить количество по названию")
    print("3. Увеличить цену всех товаров на процент")
    
    choice = input("Выберите способ редактирования (1-3): ")
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    if choice == '1':
        # Изменение цены по ID
        product_id = int(input("Введите ID товара: "))
        new_price = float(input("Введите новую цену: "))
        cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    
    elif choice == '2':
        # Изменение количества по названию
        name = input("Введите название товара: ")
        new_quantity = int(input("Введите новое количество: "))
        cursor.execute('UPDATE products SET quantity = ? WHERE name = ?', (new_quantity, name))
    
    elif choice == '3':
        # Увеличение цены на процент
        percent = float(input("Введите процент увеличения: "))
        cursor.execute('UPDATE products SET price = price * (1 + ?/100)', (percent,))
    
    else:
        print("Неверный выбор!")
        return
    
    conn.commit()
    print(f"Изменено товаров: {cursor.rowcount}")
    conn.close()

# Главное меню
def main():
    create_database()
    
    while True:
        print("\n" + "="*40)
        print("МАГАЗИН - УПРАВЛЕНИЕ БАЗОЙ ДАННЫХ")
        print("="*40)
        print("1. Показать все товары")
        print("2. Найти товар")
        print("3. Удалить товар")
        print("4. Изменить товар")
        print("5. Выход")
        
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1':
            show_all()
        elif choice == '2':
            search_products()
        elif choice == '3':
            delete_products()
        elif choice == '4':
            edit_products()
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
