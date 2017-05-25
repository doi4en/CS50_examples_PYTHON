# консервацию данных и доступ к ним через интерфейс

import pickle, shelve

print("Консервация списков.")
variety = ["огурцы", "помидоры", "капуста"]
shape = ["целые", "кубиками", "соломкой"]
brand = ["Heinz", "Чумак", "Бондюзль"]
f = open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nРасконсервация списков.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print("\nПомещение списков на полку")
s = shelve.open("pickles2.dat")
s["variety"] = ["огурцы", "помидоры", "капуста"]
s["shape"] = ["целые", "кубикамиr", "соломкой"]
s["brand"] = ["Heinz", "Чумак", "Бондюзль"]
s.sync()    # проверим, что данные записаны

print("\nИзвлечение списков из файла полки: ")
print("Торговые марки -", s["brand"])
print("Фopмы -", s["shape"])
print("Виды овощей -", s["variety"])
s.close()
