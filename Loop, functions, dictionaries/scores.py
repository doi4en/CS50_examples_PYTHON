scores = []

choice = None
while choice != "0":

    print(
    """
    Рекорды

    0 - Выход
    1 - Показать рекорды
    2 - Добавить рекорд
    """
    )

    choice = input("Baш выбор: ")
    print()

    # выход
    if choice == "0":
        print("Давай, до свидания.")

    # вьвод таблицы рекордов
    elif choice == "1":
        print("Peкopды\n")
        print("ИМЯ\tРЕЗУЛЬТАТ")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # добавление....
    elif choice == "2":
        name = input("Впишите имя игрока: ")
        score = int(input("Bnишитe его результат: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]     # списке остается только 5 рекордов

    # не правильный ввод
    else:
        print("Извините. в меню нет пункта", choice)