#Дана строка 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16',
#отражающая продажи продукции по дням в кг. Преобразовать информацию из
#строки в словари, с использованием функции найти максимальные продажи по
#каждому виду продукции, результаты вывести на экран.
def max_sales(sales_str):
    # Разделяем строку на элементы
    elements = sales_str.split()

    products = {}
    current_product = None

    for elem in elements:
        if elem.isalpha():
            # Если элемент состоит из букв, это название продукта
            current_product = elem
            products[current_product] = []
        else:
            # Иначе это число продаж, добавляем в список текущего продукта
            if current_product is not None:
                products[current_product].append(int(elem))

    # Находим максимальные продажи для каждого продукта
    max_sales_dict = {}
    for product, sales in products.items():
        max_sales_dict[product] = max(sales)

    return max_sales_dict


# Исходная строка
sales_string = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 16'

# Получаем максимальные продажи
result = max_sales(sales_string)

# Выводим результаты
for product, max_sale in result.items():
    print(f"Максимальные продажи {product}: {max_sale} кг")