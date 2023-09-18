class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

d = Dog("Tim", 34)
print(d.get_name())
print(d.get_age())
d2 = Dog("Bill", 12)
print(d2.get_name())
print(d2.get_age())
