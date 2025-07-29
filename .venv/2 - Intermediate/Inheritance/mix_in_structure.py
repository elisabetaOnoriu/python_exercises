class Loggable:
    def log(self, message):
        print(f"[LOG] {message}")


class Serializable:
    def serialize(self):
        return str(self.__dict__)


class User(Loggable, Serializable):
    def __init__(self, username):
        self.username = username


u = User("Miriam")

u.log("S-a conectat.")

print(u.serialize())
