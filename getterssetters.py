class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #getter for age
    @property
    def age(self):
        return self._age
    #setter for age
    @age.setter
    def age(self,age):
        if age<0:
            raise ValueError("age cannot be negative")
        self._age=age
    
man = person("saugat",22)
print(man.age)

try:
    man.age = -3
except ValueError as a:
    print(a)
 