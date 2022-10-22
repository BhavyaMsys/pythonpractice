from collections import OrderedDict
test_list =[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    x = str(input())
  
    test_list.append(x) 
      
print(test_list)
 
# printing original list
print("The original list : " + str(test_list))
 
# using list comprehension + OrderedDict.fromkeys() + enumerate()


y = [{val: key for key, val in enumerate(
    OrderedDict.fromkeys(test_list))}
    [z] for z in test_list]
 
# print result
print("The original list : " + str(test_list) + "  The ids of assigned values is : " + str(y) )