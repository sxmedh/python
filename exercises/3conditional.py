print("welcome to the rollercoaster")
#height = int(input("What is your height in cm? "))
height = 180
if height > 120:
    print("you can ride the rollercoaster")
    age = 15
    if age < 15:
        print("pay 5")
    elif 15 <= age <= 21:
        print("pay 10")
    else:
        print("pay 25")
else:
    print("sorry you cannot ride the rollercoaster")

if True and True:
    print("and")
if True or False:
    print("or")
if not False:
    print("not")