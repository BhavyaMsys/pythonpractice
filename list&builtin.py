a = [] # initialization of list
# mutable datatype
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
# a.append("1")
# a.extend(["2","3","4","3"])
# print(a.insert(0,"ishwar"))
# print(a.index("3"))
# print(a.count("3"))
# a.pop(-1)  # position of element
# a.remove("ishwar") # value of element
# a.reverse() 
# a.sort(reverse=True)
# b = []
# b = a.copy()
# print(id(a))
# print(id(b))
# c = a
# print(id(c))
# print(a)
# print(b)
# print(a)
# print(c)
# a.clear()
# print(a)
# print(b)
# print(c)

# buitin fuction
# abs()	Returns the absolute value of a number
# all()	Returns True if all items in an iterable object are true
# any()	Returns True if any item in an iterable object is true
# ascii()	Returns a readable version of an object. Replaces none-ascii characters with escape character
# bin()	Returns the binary version of a number
# bool()	Returns the boolean value of the specified object
# bytearray()	Returns an array of bytes
# bytes()	Returns a bytes object
# callable()	Returns True if the specified object is callable, otherwise False
# chr()	Returns a character from the specified Unicode code.
# classmethod()	Converts a method into a class method
# compile()	Returns the specified source as an object, ready to be executed
# complex()	Returns a complex number
# delattr()	Deletes the specified attribute (property or method) from the specified object
# dict()	Returns a dictionary (Array)
# dir()	Returns a list of the specified object's properties and methods
# divmod()	Returns the quotient and the remainder when argument1 is divided by argument2
# enumerate()	Takes a collection (e.g. a tuple) and returns it as an enumerate object
# eval()	Evaluates and executes an expression
# exec()	Executes the specified code (or object)
# filter()	Use a filter function to exclude items in an iterable object
# float()	Returns a floating point number
# format()	Formats a specified value
# frozenset()	Returns a frozenset object
# getattr()	Returns the value of the specified attribute (property or method)
# globals()	Returns the current global symbol table as a dictionary
# hasattr()	Returns True if the specified object has the specified attribute (property/method)
# hash()	Returns the hash value of a specified object
# help()	Executes the built-in help system
# hex()	Converts a number into a hexadecimal value
# id()	Returns the id of an object
# input()	Allowing user input
# int()	Returns an integer number
# isinstance()	Returns True if a specified object is an instance of a specified object
# issubclass()	Returns True if a specified class is a subclass of a specified object
# iter()	Returns an iterator object
# len()	Returns the length of an object
# list()	Returns a list
# locals()	Returns an updated dictionary of the current local symbol table
# map()	Returns the specified iterator with the specified function applied to each item
# max()	Returns the largest item in an iterable
# memoryview()	Returns a memory view object
# min()	Returns the smallest item in an iterable
# next()	Returns the next item in an iterable
# object()	Returns a new object
# oct()	Converts a number into an octal
# open()	Opens a file and returns a file object
# ord()	Convert an integer representing the Unicode of the specified character
# pow()	Returns the value of x to the power of y
# print()	Prints to the standard output device
# property()	Gets, sets, deletes a property
# range()	Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()	Returns a readable version of an object
# reversed()	Returns a reversed iterator
# round()	Rounds a numbers
# set()	Returns a new set object
# setattr()	Sets an attribute (property/method) of an object
# slice()	Returns a slice object
# sorted()	Returns a sorted list
# staticmethod()	Converts a method into a static method
# str()	Returns a string object
# sum()	Sums the items of an iterator
# super()	Returns an object that represents the parent class
# tuple()	Returns a tuple
# type()	Returns the type of an object
# vars()	Returns the __dict__ property of an object
# zip()	Returns an iterator, from two or more iterators
list = ["abcd","abc","a","ab"]
list1 = ["ishwar","j","lal","karan"]
print(len(list1))
print(min(list,key=len))
print(min(list1,key=len))
print(max(list1,key=len))
print(sorted(list1,key=len))
a = [10,20,30,40,50]
print(sum(a))
print(bin(10))
print(oct(10))

print(any(a))
b = slice(1,3)
print(a[1:3])
print(repr(a))

c = 10.55555555000521554841515
print(round(c,2))

print(pow(10,2))
print(type(a))

print(tuple(a))

# a =[i for i in zip(a)]
# print(a)
a = bool(0)
print(a)

a = "10"
print(type(eval(a)))
for i in range(10,20):
    t = "hello {}".format(i)
    print(t)


# a = 97
# A = 65



