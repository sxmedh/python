import random
# Split string method
names_string = "a, b, c, d, e"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = len(names)

num = random.randint(0,length-1)

print(names[num])