# Закрытая зверюшка


class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка!")
        self.name = name            # открытый атр~бут
        self.__mood = mood          # закрытый атрибут

    def talk(self):
        print("\nMeня зовут", self.name)
        print("Ceйчac я чувствую себя", self.__mood, "\n")

    def __private_method(self):
        print("Этo закрытый метод.")

    def public_method(self):
        print("Этo открытый метод.")
        self.__private_method()

# main
crit = Critter(name = "Бобик", mood = "прекрасно")
crit.talk()
crit.public_method()

"""
print(crit.mood)
Traceback (most recent call last):
File "<pyshell#l>". line 1. in <module>
pri nt ( crit. mood)
AttributeError: 'Critter' object has no attribute 'mood'
"""