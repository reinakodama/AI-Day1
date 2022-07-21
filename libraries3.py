#from module import some_function as some_name
from math import pow as exponent
from math import sqrt as squareroot
from random import shuffle as mixup
from random import randint as chooseint
from random import choice as chooseitem

result_1 = exponent(2,4)
print("result_1 is",result_1)
result_2 = squareroot(16)
print("result_2 is", result_2)
result_3 = chooseint(0,100)
print("result_3 is", result_3)
names = ["Reina","Inacio","Elena","Waka","Jess"]
print("Original names: ",names)
mixup(names)
print("Names after shufflong: ",names)
result_4 = chooseitem(names)
print("Chosen name is: ",result_4)