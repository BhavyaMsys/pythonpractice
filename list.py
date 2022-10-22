# list = ["ram", "shyam", "mohan", "Apple", "Orange","Pineapple"]
# print(list)
# print(len(list))
#====================================================================
list1 = ["Delhi", "Punjab","Uttar Pradesh","Bambay","Kolkata"]
list2 = ["11","22","33","44","55","66"]
list3 = list1

print(list2)

print(list1)

print(type(list1))

print(len(list2))

print(list1[2])

print(list1[1:4])

print(list1[:3])

print(list2[-2] )

print(list2[4:])
#====================================================================

list2[2:4] = ["77"]
print(list2)
#====================================================================

list2.insert(6,"77")
print(list2)
#====================================================================

if "Mumbai" in list1:
  print("Yes! Mumbai is in this list1")
else:
  print("No!! Mumbai is not is this list1")    

#====================================================================
list1 = list3

for x in list3:
    print(x)
#====================================================================

list1.extend(list2)
print(list1)
#====================================================================

list1.remove("Punjab")
print(list1)
#====================================================================

list2.pop(2)
print(list2)
#====================================================================

list2.clear()
print(list2)
#====================================================================


