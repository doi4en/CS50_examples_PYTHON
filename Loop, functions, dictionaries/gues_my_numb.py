import random

print("\tWelcome!")
my = int(input("Your number between 1 and 100: "))
min = 0
max = 100
the_number = 0
tries = 0

while the_number != my:
        the_number = random.randint(min, max)

        if the_number < my:
                min = the_number
        else:
                max = the_number
        tries += 1


print("it only took you", tries, "tries!\n")
print("Bingo. Your number is ", the_number, "\n")
