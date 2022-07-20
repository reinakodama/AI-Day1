class Student:
    def __init__(self, name, age, grade, GPA):
        self.name = name
        self.age = age
        self.grade = grade
        self.GPA = GPA
    def introduce_self(self):
        print("Hi I'm " + self.name)

s1 = Student("Reina", 16, "10th", 4.0)
s1.introduce_self()

class Course:
    def __init__(self, name, professor, duration, difficulty):
        self.name = name
        self.professor = professor
        self.duration = duration
        self.difficulty = difficulty
    def course_detail(self):
        print("The course" , self.name , "is taught by" , self.professor , "and is" + self.duration , "long. It is said to be a difficulty level" , self.difficulty , "out of 10.")

c1 = Course("AI", "Benedict", "3 weeks", 7)
c1.course_detail()