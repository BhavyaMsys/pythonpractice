#find shape according to dimension
#rectangle
#square
#equilateral triangle

def find_shape(a=None,b=None,c=None,d=None):
    if a==b and b==c and c==d and d==a:
        return print("It is a Square")
    elif a==b and c==d or b==c and a==d or a==c and b==d:
        return print("It is a rectangle")
    elif a==b==c or b==c==d or a==c==d or a==b==d:
        return print("It is a triangle")
    else:print("No shape possible")
    
a=input("Enter the value:")
b=input("Enter the value:")
c=input("Enter the value:")
d=input("Enter the value:")
a= int(a) if a else None
b= int(b) if b else None
c= int(c) if c else None
d= int(d) if d else None

find_shape(a,b,c,d)

