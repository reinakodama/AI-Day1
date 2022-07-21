#from module import some_function
from math import sqrt,pow
from random import shuffle,randint,choice

result_1 = pow(2,4)
print("result_1 is",result_1)
result_2 = sqrt(16)
print("result_2 is", result_2)
result_3 = randint(0,100)
print("result_3 is", result_3)
names = ["Reina","Inacio","Elena","Waka","Jess"]
print("Original names: ",names)
shuffle(names)
print("Names after shufflong: ",names)
result_4 = choice(names)
print("Chosen name is: ",result_4)