#pattern1
row =8
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end="")
    print("")


#sum of n terms
s=0
a=int(input())
for i in range(1,a+1,1):
    s+=i
print("sum=",s)

#multiplication
x=int(input())
for i in range(1,11,1):
    product=x*i
    print(product)

#pattern2
n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()

