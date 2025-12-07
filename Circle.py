class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = radius  # приватный атрибут
    def get_radius(self):
        return self._radius
    def set_radius(self, new_radius):
        if new_radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self._radius = new_radius

# Пример использования:
if __name__ == "__main__":
    # 1 Объект класса Circle
    circle = Circle(7)
    print(f"Начальный радиус: {circle.get_radius()}")
    # 2 Изменяем радиус
    circle.set_radius(11)
    # 3 Выводим новый радиус на экран
    print(f"Новый радиус: {circle.get_radius()}")
