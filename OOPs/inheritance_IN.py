class User:
    def login(self):
        print("login")
    def Register(self):
        print("Register")

class Student(User):
    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")

stu1=Student()

stu1.login()
stu1.Register()
stu1.review()


