#2
class InvalidPasswordError(Exception):
    def __init__(self, password):
        self.password = password
class InvalidPasswordNumberError(Exception):
    def __init__(self, password):
        self.password = password
def valide_password(password):
    if len(password) < 8:
        raise InvalidPasswordError(password)
    for i in password:
        if i != 1:
            raise InvalidPasswordNumberError(password)
        if i != 2:
            raise InvalidPasswordNumberError(password)
        if i != 3:
            raise InvalidPasswordNumberError(password)
        if i != 4:
            raise InvalidPasswordNumberError(password)
        if i != 5:
            raise InvalidPasswordNumberError(password)
        if i != 6:
            raise InvalidPasswordNumberError(password)
        if i != 7:
            raise InvalidPasswordNumberError(password)
        if i != 8:
            raise InvalidPasswordNumberError(password)
        if i != 9:
            raise InvalidPasswordNumberError(password)
        if i != 0:
            raise InvalidPasswordNumberError(password)
    else:
        print("Пароль прийнято")

try:
    password = input("Введіть пароль: ")
    valide_password(password)
except InvalidPasswordError as a:
    print(f"Неправильний пароль {a.password} \n"
          f"Треба мінімум 8 символів")