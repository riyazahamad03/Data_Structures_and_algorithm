from re import A


class Myclass():
    def __init__(self,name,age):
        self.name = name
        self.age=age
    # def __str__(self) -> str:
    #     return f"{self.name} ({self.age}) ({self.Graduationyear})"
class SubClass(Myclass):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.Graduationyear = year
    def WelcomeMessage(self):
        return f"Name : {self.name} \nAge : {self.age} \nGraduationYear : {self.Graduationyear}"
# print("------------------- Welcome To Classes and Objects Implementation ---------------------------------")
name = input("Please Enter Your Name : ")
age = int(input("Please Enter Your Age : "))
year = int(input("Please Enter Your Graduation Year : "))
print("------------------- Welcome To Classes and Objects Implementation ---------------------------------")
pl = SubClass(name,age,year)
print(pl.WelcomeMessage())