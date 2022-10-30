#fbonaci series
num1=0
num2=1
print("Fibonacci sequence:")

for i in range(10):
    
    print(num1, end="  ")
    
    res = num1 + num2
    num1 = num2
    num2 = res
#factorial
number = 5
factorial = 1
if number < 0:
    print("Factorial does not exist for negative numbers")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for j in range(1, number + 1):
        # multiply factorial by current number
        factorial = factorial * j
    print("\nThe factorial of", number, "is", factorial)
