class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Rectangle(Figure):
    pass  # Прямоугольник использует методы родительского класса


class Square(Figure):
    def __init__(self, side):
        # У квадрата ширина и высота равны, поэтому передаем side и в width, и в height
        super().__init__(side, side)

    # Переопределяем методы, так как для квадрата можно оптимизировать вычисления
    def area(self):
        return self.width ** 2  # или self.height ** 2

    def perimeter(self):
        return 4 * self.width  # или 4 * self.height


# Пример использования
rectangle = Rectangle(4, 5)
print("Прямоугольник:")
print(f"Ширина: {rectangle.width}, Высота: {rectangle.height}")
print(f"Площадь: {rectangle.area()}")
print(f"Периметр: {rectangle.perimeter()}")

square = Square(3)
print("\nКвадрат:")
print(f"Сторона: {square.width}")  # или square.height, так как они равны