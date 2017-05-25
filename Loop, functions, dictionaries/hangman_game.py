import random

# константы
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   |
 |   |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |
----------
""")

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("ЗАДАЧА", "ЧАЙ", "МОЛОКО", "СЫР", "ПИТОН")

# обьявление переменных
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []


print("Дoбpo пожаловать в игру 'Виселица'. Удачи вам!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nBы уже предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)

    guess = input("\n\nВведите букву: ")
    guess = guess.upper()

    while guess in used:
        print("Bы уже предлагали букву", guess)
        guess = input("\n\nBвeдитe букву: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nДa! Буква", guess, "есть в слове!")


        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new

    else:
        print("\nK сожалению. буквы", guess, "нет в слове.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nBac повесили!")
else:
    print("\nBы отгадали!")

print("\nБылo загадано слово", word)
