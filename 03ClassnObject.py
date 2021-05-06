class Person:  ##start class
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def myfunc(self):
        print ("hello my name is " + self.name)

p1 = Person("Jhon", 36) #start object

print(p1.name)
print(p1.age)

##test 2 with function
print ("with function")
p2 = Person("wahid", 356)
p2.myfunc()