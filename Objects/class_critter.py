class Critter(object):
    """Виртуальный питомец"""
    total = 0

    @staticmethod
    def status():
        print("\nBcero зверюшек сейчас", Critter.total)

    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1

#main
print("Haxoжy значение атрибута класса Critter.total :", end=" ")
print(Critter.total)

print("\nCoздaю зверюшек.")
crit1 = Critter("зверюшка 1")
crit2 = Critter("зверюшка 2")
crit3 = Critter("зверюшка 3")
crit4 = Critter("зверюшка 3")

Critter.status()

print("\nOбpaщaюcь к атрибуту класса через объект:", end= " ")
print(crit1.total)