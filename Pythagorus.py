def pythagorus(p,b,h):
    if p**2+b**2==h**2:
        print("It proves Pythagorus theorem")
    else:
        print("No pythagorus")
p=int(input("Enter value of Perpendicular:"))
b=int(input("Enter value of base:"))
h=int(input("Enter value of hypotaneous:"))
pythagorus(p,b,h)