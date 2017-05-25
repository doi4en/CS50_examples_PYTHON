class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += "имя: " + self.name + "\n"
        return rep

    def talk(self):
        print("Привет. Меня зовут", self.name, "\n")

# main
crit1 = Critter("Бoбик")
crit1.talk()

crit2 = Critter("Мурзик")
crit2.talk()

print("Bывoд объекта critl на экран:")
print(crit1)
print(crit2)
print("Непосредственный доступ к атрибуту crit1.name:")
print(crit1.name)