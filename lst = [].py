l1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = str(input())
    l1.append(x)
obj = enumerate(l1)
#print ("Return type:", type(obj))
print (list(enumerate(l1)))