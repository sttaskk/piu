class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"
# Пример:
if __name__ == "__main__":
    # 1. Объект базового класса Vehicle
    vehicle = Vehicle("Название1", "Модель1")
    print("Информация о транспортном средстве:")
    print(vehicle.get_info())
    # 2. Объект класса Car
    car = Car("Название2", "Модель2", "Дизель")
    print("\nИнформация о автомобиле:")
    print(car.get_info())
    # 3. Ещё один пример автомобиля
    gas_car = Car("Название3", "Модель3", "Бензин")
    print("\nЕщё один автомобиль:")
    print(gas_car.get_info())
