# Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во".

class Product:
    def __init__(self, name, price, quantity):
        self.name = name        # Название товара
        self.price = price      # Цена товара
        self.quantity = quantity  # Количество товара
    
    def display_info(self):
        # Выводит информацию о товаре в заданном формате
        print(f"Название: {self.name}, Цена: {self.price}, Количество: {self.quantity}")


# Пример использования
product1 = Product("Яблоки", 50, 10)
product1.display_info()