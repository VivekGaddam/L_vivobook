class Student():
    def __init__(self,rono,name) -> None:
        self.rono=rono
        self.name=name
    def add(self,a,b,c):
        return a+b+c
    def add(self,a,b,c,d=0):
        return a+b+c+d
viv=Student(36,'vivek')        
print(viv.add(1,2,3,4))
print(viv.add(1,2,3))

class Teacher(Student):
    def __init__(self,rono,name,subject) -> None:
        super().__init__(name,rono)
        self.subject=subject
    def add(self):
        print('na modda undhi eda em ledhu')

msd=Teacher(89,'vivek',"oops")
print(msd.add())
