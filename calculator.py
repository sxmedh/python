import art 
print(art.logo)


def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

dictionary_operation = {"+":add,
                        "-":sub,
                        "*":mult,
                        "/":div,
                        }

def calculate(num1,num2):
    for key in dictionary_operation:
        print(key)
    operation_sym = input("which operation do you want to perform?")
    operation = dictionary_operation[operation_sym]
    result = operation(num1,num2)
    
    return result


num1 = int(input("what is the first number?"))
num2 = int(input("what is the second number?"))
result = calculate(num1,num2)
print(result)
choice = input("Do you want to perform more operations? y/n ")
while(choice == 'y'):
    x = int(input("Enter number: "))
    result = calculate(result,x)
    print(result)
    choice = input("Do you want to perform more operations? y/n ")

print(result)     