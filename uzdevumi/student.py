# -*- coding: utf-8 -*-
class Students:
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english

    def ave(self):
        self.average = (self.math + self.science + self.english) / 3

    def show(self):
        self.ave()
        print("Name: ", self.name)
        print("Math Grade: ", self.math)
        print("Science Grade: ", self.science)
        print("English Grade: ", self.english)
        if self.average >= 7.5:
            self.status = "Passed"
        else:
            self.status = "Failed"
        print("Average Grade: {} ({})".format(round(self.average,0), self.status))

print()
print("Student Average Grade")
print()
Name = str(input("Enter Name: "))
Math = float(input("Enter Math: "))
Science = float(input("Enter Science: "))
English = float(input("Enter English: "))
print()

stud = Students(Name, Math, Science, English)
stud.show()
