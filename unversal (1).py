# from keyword import kwlist
# print(kwlist)

# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# print(len(kwlist))

# syntex of of fuction
# def function_name(arguments):
#     # business logic
#     return variable

# requirements
# operator
# conditions
# function
# while loop
# string formating

# 1. calculator program by using fuction
# 2. calculator program by using anynomus function

#1.
def addition(x,y):
    "it will return sum of two values"
    return x+y

def substraction(x,y):
    "it will return positive value only after substraction"
    if x>y:
        return x-y
    else:
        return y-x

def multipcation(x,y):
    "It will return product of two values"
    return x*y

def division(x,y):
    "It will return float value after division"
    if x==0 or y==0:
        return ZeroDivisionError
    elif x>y:
        return x/y
    else:
        return y/x
def flore_division(x,y):
    "It will return integer value after division"
    if x==0 or y==0:
        return ZeroDivisionError
    elif x>y:
        return x//y
    else:
        return y//x

def exponent(x,y):
    "It will return y is power of x value"
    return x**y

def remainder(x,y):
    "It will return remainder after division"
    return x%y


while True: # infinite loop
    q = str(input("press any key to start program and q for quit:")).upper()
    if q=="Q":
        print("Thnak you for using this program")
        break
    else:
        print("""
        1 for addition
        2 for substraction
        3 for multipication
        4 for division
        5 for flore division
        6 for exponent
        7 for remainder
        
        """)
        choose = int(input("please select option from above:"))
        try:
            if choose==1:
                a = float(input("please enter the first number:"))
                b = float(input("please enter the second number:"))
                print(f"{addition(a,b)} is the sumation of {a} and {b}")
            elif choose==2:
                a = float(input("please enter the first number:"))
                b = float(input("please enter the second number:"))
                print(f"{substraction(a,b)} is the substraction of {a} and {b}")
            elif choose==3:
                a = float(input("please enter the first number:"))
                b = float(input("please enter the second number:"))
                print(f"{multipcation(a,b)} is the multipication of {a} and {b}")
            elif choose==4:
                a = float(input("please enter the first number:"))
                b = float(input("please enter the second number:"))
                print(f"{division(a,b)} is the devision of {a} and {b}")
            elif choose==5:
                a = float(input("please enter the first number:"))
                b = float(input("please enter the second number:"))
                print(f"{flore_division(a,b)} is the flore devision of {a} and {b}")
            elif choose==6:
                a = float(input("please enter the first number:"))
                b = float(input("please enter the second number:"))
                print(f"{exponent(a,b)} is the exponent value of {a} and {b}")
            elif choose==7:
                a = float(input("please enter the first number:"))
                b = float(input("please enter the second number:"))
                print(f"{remainder(a,b)} is the exponent value of {a} and {b}")
            else:
                print("please choose the correct option")
        except:
            print("please give the input in number format")


        







    










