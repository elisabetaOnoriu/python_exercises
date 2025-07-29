class Employee:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def get_role(self):
        return "Manager"


class Director(Manager):
    def get_role(self):
        return "Director"


e = Employee("Ana")
m = Manager("Mihai")
d = Director("Daria")

print(e.name, "-", e.get_role())
print(m.name, "-", m.get_role())
print(d.name, "-", d.get_role())
