
# Question: Subclass Initialization

# Create a class Person with an __init__ method that takes a name as a parameter. 
# Create a subclass Employee that inherits from Person and adds an attribute position.
# Instantiate an Employee object and print the name and position using that object
# You can give any name and position values you want

class person:
    def __init__(self, name) -> None:
        self.name = name

#Write your code here


#challenge Question

class A:
    def __init__(self, x):
        self.x = x

    def display(self):
        print("A:", self.x)

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def display(self):
        print("B:", self.x, self.y)

class C(A):
    def __init__(self, x, z):
        super().__init__(x)
        self.z = z

    def display(self):
        print("C:", self.x, self.z)

class D(B, C):                                  #D inherits values and methods from Both, B and C
    def __init__(self, x, y, x1, z, w):
        B.__init__(self, x, y)
        C.__init__(self, x1, z)  
        self.w = w

    def display(self):
        print("D:", self.x, self.y, self.z, self.w)


    def display(self):
        print("D:", self.x, self.y, self.z, self.w)

obj = D('a', 'b', 'c', 'd', 'e')
obj.display()                         #What would be the output, explain how we got that particualr output