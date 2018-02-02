import json


class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)


dog = Dog("Шарик", "Доберман")


class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })


class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super().__init__(name, breed)


print(ExDog("Макс", "пудель").breed)


class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name)
        self.breed = "Шерстяная собака породы {0}".format(breed)


print(WoolenDog("Шарик", "овчарка").breed)
