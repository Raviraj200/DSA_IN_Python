# class User:
#     def login(self):
#         print("login")
#     def Register(self):
#         print("Register")

# class Student(User):
#     def enroll(self):
#         print("Enroll")
#     def review(self):
#         print("Review")

# stu1=Student()

# stu1.login()
# stu1.Register()
# stu1.review()

class min_class:
    def __init__(self,last):
        self.__last=last

    def __show(self):
        print(self.__last)    

    def moreShow(self):
        return self.__show()    

class second(min_class):
    pass
    

obj = second("ravi")
obj.moreShow()

