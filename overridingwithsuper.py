class A:
    classvar1 = "I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"
        

class B(A):     # Class B inherit Class A
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()# without super keyword error occur../ with super keyword you can access base class method with same name..
        print(super().classvar1)# In output without super derived(class B) variable show

a = A()
b = B()
#first of all run __init__ constructor
print(b.special, b.var1, b.classvar1)# As you see in output  variable override with same name
