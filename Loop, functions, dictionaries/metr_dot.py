# Maitre D'
# Demonstrates treating a value as a condition

print("Дoбpo пожаловать в Шато-де-Перекуси!")
print("Kaжeтcя. нынешним вечером у нас все столики заняты.\n")

money = int(input("Cкoлькo долларов вы готовы дать метрдотелю на чай? "))

if money:
    print("Прошу прощения. мне сейчас сообщили. что есть один свободный столик. Сюда пожалуйста.")
else:
    print("Присаживайтесь. будьте добры. Придется подождать.")