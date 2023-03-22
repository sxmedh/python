file = open("text.txt")
contents = file.read()
print(contents)
file.close()

with open("text.txt") as file2:
    contents2 = file2.read()
    print(contents2)

with open("text.txt", mode="w") as file3:
    file3.write("new text.")

with open("text.txt", mode="a") as file3:
    file3.write("\nthis is the new text")
