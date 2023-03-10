num = int(input("enter a number "))

def prime(num):
    check = True
    for i in range (2,num):
        if num%i == 0:
            check = False
    return check

check = prime(num)

print(check)