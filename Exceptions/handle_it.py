# обработка исключительных ситуаций

# try/except
try:
    num = float(input("1.Bвeдитe число: "))
except:
    print("Пoxoжe, это не число!")

# specifying exception type
try:
    num = float(input("\n2.Bвeдитe число: "))
except ValueError:
    print("Этo не число!")

# handle multiple exception types
print()
for value in (None, "Hi!"):
    try:
        print("3.Пытаюсь преобразовать в число", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Пoxoжe, это не число!")

print()
for value in (None, "Hi!"):
    try:
        print("4.Пытаюсь преобразовать в число", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я умею преобразовывать только строки и числа!")
    except ValueError:
        print("Я умею преобразовывать только строки, составленные из цифр!")

# get an exception's argument
try:
    num = float(input("\n5.Bвeдитe число: "))
    d = 1/ num
except ValueError as e:
    print("Этo не число! Интерпретатор как бы говорит нам...")
    print(e)
except ZeroDivisionError as i:
    print("Ошибка! Интерпретатор как бы говорит нам...")
    print(i)


# try/except/else
try:
    num = float(input("\n6.Bвeдитe число: "))
except ValueError:
    print("Этo не число!")
else:
    print("Bы ввели число", num)