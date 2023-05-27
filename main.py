#2
class UserNotFoundError(Exception):
    def __init__(self, username):
        self.username = username
class UserDatabase:
    def __init__(self):
        self.vocabulary = {"sjds": {"name": "Ната", "age": 13},
            ".hjkj": {"name": "Настя", "age": 16},
            "3odkw3": {"name": "Макс", "age": 26} }

    def get_user(self, username):
        if username in self.vocabulary:
            return self.vocabulary[username]
        else:
            raise UserNotFoundError(username)

database = UserDatabase()
try:
    user = database.get_user(".hjkj")
    print(f"Користувач {user} є в цій базі даних")
except UserNotFoundError as a:
    print(f"Користувача {a.username} немає в цій базі даних\n"
          f"Спробуйте ще раз")