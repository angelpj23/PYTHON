print ("1-Sum")
print ("2-Subtraction")
print ("3-Multiplication")
print ("4-Division")
print ("5-Empowerment")
print ("6-Radical")
print ("7-Exit")

from math import sqrt, pow

def Sum(n1, n2):
    return n1 + n2
def Subtraction(n1, n2):
    return n1 - n2
def Multiplication(n1, n2):
    return n1 * n2
def Division(n1, n2):
    return n1 / n2
def Empowerment(n1, n2):
    return pow (n1, n2)
def Radical(n1):
    return sqrt(n1)
try:
    while True:
        option = int(input("Select an available number option:\n"))
        if option > 0 and option <=7:
            if option > 0 and option <=5:
                n1 = int(input("Enter first number: "))
                n2 = int(input("Enter second number: "))
    
            elif option == 6:            
                n1 = int(input("Enter a number:\n "))

            if option == 1:
                print(Sum(n1, n2))
            elif option == 2:
                print(Subtraction(n1, n2))    
            elif option == 3:
                print(Multiplication(n1, n2))
            elif option == 4:
                try:
                    print(Division(n1, n2))
                except:
                    print ("cannot be divided by 0")
            elif option == 5:
                print(Empowerment(n1, n2))
            elif option == 6:
                print(Radical(n1))
            elif option == 7:
                print("Bye! come back soon")
                break
except ValueError:
    print("only numbers are allowed")