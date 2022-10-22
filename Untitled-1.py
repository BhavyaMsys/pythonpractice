class studentlist:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = studentlist("John", 18)
p2 = studentlist("Abhi", 21)
p3 = studentlist("Jack", 20)
p4 = studentlist("Karan", 17)

print([p1.name,p1.age])
print([p2.name,p2.age])
print([p3.name,p3.age])
print([p4.name,p4.age])

