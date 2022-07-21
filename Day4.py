import math #built-in python module that gives users access to various mathematical operations and functions
import random #built-in python module with various functions to generate random numbers and perform many probability operations

result_1 = math.pow(2,4) #access the pow(x,y) function in the math module, computes x exponent y
print("result_1 is",result_1)
result_2 = math.sqrt(16) #access the sqrt(x) function in the math module, computes square root of x
print("result_2 is", result_2)
result_3 = random.randint(0,100) #access the randint(x,y) function in the random module, returns a random integer between x and y
print("result_3 is", result_3)
names = ["Reina","Inacio","Elena","Waka","Jess"]
print("Original names: ",names)
random.shuffle(names) #access the shuffle(x) function in the random module, shuffles the elements in the collection of elements x
print("Names after shufflong: ",names)
result_4 = random.choice(names) #access the choice(x) function in the random module, makes a random choice from the elements in the collection x
print("Chosen name is: ",result_4)

from Day3 import Student
from Day3 import Course

student1 = Student("Erika", 19, "12th", 3.8)
course1 = Course("FOOP", "Kaneko", "yearlong", 5 )
course1.course_detail()
student1.introduce_self()

