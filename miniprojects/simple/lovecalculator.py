# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
numtrue = 0
numtrue += name1.count("t")
numtrue += name1.count("r")
numtrue += name1.count("u")
numtrue += name1.count("e")
numtrue += name2.count("t")
numtrue += name2.count("r")
numtrue += name2.count("u")
numtrue += name2.count("e")

numlove = 0
numlove += name1.count("l")
numlove += name1.count("o")
numlove += name1.count("v")
numlove += name1.count("e")
numlove += name2.count("l")
numlove += name2.count("o")
numlove += name2.count("v")
numlove += name2.count("e")

print(str(numtrue)+str(numlove))

