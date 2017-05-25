# запись....

print("Coздaю текстовый файл методом write()")
text_file = open("write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()

print("\nЧитaю вновь созданный файл.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()

print("\nСоздаю текстовый файл методом writelines().")
text_file = open("write_it.txt", "w")
lines = ["Line 1\n",
         "This is line 2\n",
         "That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()

print("\nЧитaю вновь созданный файл.")
text_file = open("write_it.txt", "r")
print(text_file.read())
text_file.close()
