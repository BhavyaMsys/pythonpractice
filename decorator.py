def A(text):
    return text.upper()
 
def B(text):
    return text.lower()
 
def C(func):
    # storing the function in a variable
    greet = func("Decorator function.")
    print (greet)
 
C(A)
C(B)