class employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last
        
    
    @property
    def email(self):
        return f'{self.first}{self.last}+@email.com'

    @property       
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self,value):
        self.first,self.last=value.split(' ')
        
    @fullname.deleter
    def fullname(self):
        print("delete name!")
        self.first=None
        self.last=None

    
emp_1=employee("anuh",'giri')
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
emp_1.fullname="himanshu bista"


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

    