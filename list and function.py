
def multiplication(my_List):
 
    # Multiply elements one by one
    result = 1
    for a in my_List:
        result = result * a
    return result
#taking list as input from user
try:
    X = []

      
    while True:
        X.append(int(input()))          
except:
    print(X)
try:
    Y = []

      
    while True:
        Y.append(int(input()))          
except:
    print(Y)

print(f"{multiplication(X)} is the multiplication of {X}")
print(f"{multiplication(Y)} is the multiplication of {Y}")
    


