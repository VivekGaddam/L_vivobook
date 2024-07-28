#inheritance
'''
class Person() :
    def __init__(self,age,gender) -> None:
        self.age=age
        self.gender=gender
    def __str__(self):
        return f"Gender:{self.gender} of age :{self.age}"
class Student(Person):
    def __init__(self,age,gender,sec,roll_no) -> None:
        Person.__init__(age,gender)
        self.sec=sec
        self.roll_no=roll_no
v=Person(20,'male')
vivek=Student(20,'male','c_1',36)
print(v)

'''
class Person(object):
    def __init__(self, age, gender) -> None:
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f"Gender: {self.gender} of age: {self.age}"

class Male(object):
    @staticmethod
    def HAS():
        return 'HAS A penis'

class Student(Person, Male):
    def __init__(self, age, gender, sec, roll_no) -> None:
        # Initialize the Person part of Student
        Person.__init__(self, age, gender)
        # Optionally, initialize the Male part if specific attributes are needed
        if self.gender.lower() == 'male':
            Male.__init__(self)
        self.sec = sec
        self.roll_no = roll_no

    def __str__(self):
        return super().__str__() + f", Section: {self.sec}, Roll No: {self.roll_no}"

# Test the code
v = Person(20, 'male')
vivek = Student(20, 'male', 'c_1', 36)
print(vivek.HAS())  # Call the HAS method from the Male class
print(v)
print(vivek)
import numpy as np
a=np.random.randint(2,7,10)
print(a)