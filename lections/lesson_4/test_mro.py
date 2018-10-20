
class Alive(object):
    @property
    def its_me(self):
        return f"I am {self.__class__.__name__}"


class Animal(Alive):
    pass


class Herb(Alive):
    pass


class ComplicatedHerb(Herb):
    pass


class Plant(ComplicatedHerb):
    pass


class UFO:
    pass


class Monkey(Alive, UFO):
    pass


class Human(Monkey):
    pass


class ModernHuman(Alive, Plant):
    pass


# print(ModernHuman().its_me)
print()

for cls in ModernHuman.mro():
    print(cls.__name__, end=" -> ")
else:
    print("AttributeError")
