def addition(x,y):
    "It will return sum of 2 number"
    return x+y
def substraction(x,y):
    "it will return positive subratction"
    if x>y:
        return x-y
    else:
        return y-x
def multiplication(x,y):
    "product of 2 numbers"
    return x*y
def divisionn(x,y):
    "return float value"
    if x==0 or y==0:
        return ZeroDivisionError
    elif x>y:
        return x/y
    else:
        return y/x
while True:
    q = str (input("press any key to start and q for quit")).upper()
    if q=="Q":
        print("Thank you")
        break
    else:
        print("""
        1. Addition
        2. Subtratction
        3. Multiplication
        4. Division
        """)
    choose==int(input("please select option"))
    try:
    if choose==1:
        a= float(input("1st Number:"))
        b= float(input("2nd Number:"))
        print(f"{addition(a,b) is the addition of {a} and {b}")
    except:
        print("Provide input in number form")
