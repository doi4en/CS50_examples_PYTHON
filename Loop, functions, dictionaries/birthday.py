#Позиционные параметры

def birthday1(name, age):
    print("С днем рождения,", name, "!", " я слышал тебе", age, "сегодня.\n")

# Параметры со значениями по умолчанию
def birthday2(name = "Вася", age = 1):
    print("С днем рождения,", name, "!", " я слышал тебе", age, "сегодня.\n")


#birthday1("Вася", 1)
#birthday1(1, "Вася")
#birthday1(name = "Вася", age = 1)
#birthday1(age = 1, name = "Вася")

birthday2()
birthday2(name = "Федя")
birthday2(age = 12)
birthday2(name = "Федя", age = 12)
birthday2("Федя", 12)