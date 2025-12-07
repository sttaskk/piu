class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._password = password  # приватный атрибут
    def set_password(self, new_password):
        if not new_password:
            raise ValueError("Пароль не может быть пустым")
        self._password = new_password
        print("Пароль успешно изменён")
    def check_password(self, password):
        return self._password == password
# Пример:
if __name__ == "__main__":
    # 1. Объект класса UserAccount
    user = UserAccount("anastasia", "potntiaa@mail.ru", "potntiaa777")
    # 2. Проверка текущего пароля
    print("Проверка исходного пароля:")
    print(user.check_password("potntiaa777"))  # True
    print(user.check_password("potntiaa777."))  # False
    # 3. Изменение пароля
    user.set_password("potntiaa777.")
    # 4. Проверка нового пароля
    print("\nПроверка нового пароля:")
    print(user.check_password("potntiaa777."))  # True
    print(user.check_password("potntiaa777"))  # False
