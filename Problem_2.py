class Person():
    def __init__(self,name,email) -> None:
        self.name=name
        self.email=email
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def introduction(self):
        print(f"Hello my name is {self.name}")
class Student(Person):
    def __init__(self,name,email,student_id,branch) -> None:
        super().__init__(name,email)
        self.student_id=student_id
        self.branch=branch
    def get_student_id(self):
        return self.student_id
    def get_branch(self):
        return self.branch
    def introduction(self):
        print(f"hello Iam{self.name},a student studying in {self.branch}")
class Faculty(Person):
    def __init__(self,name,email,department,courses) -> None:
        super(Person).__init__(name,email)
        self.department=department
        self.courses=courses
    def get_department(self):
        return self.department
    def get_courses(self):
        return self.courses
    def introduction(self):
        print(f"Helllo iam {self.name} iam faculty")

vivek=Student("Vivek","Vivek@gmail.com",student_id=36,branch="CSE")
print(vivek.get_name())