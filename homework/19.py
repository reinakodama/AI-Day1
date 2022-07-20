def prac1(numOfHours):
    result = numOfHours*60
    print(result)

def prac2(minHour):
    if(minHour<60):
        result=minHour*60
        print(result)
    elif(minHour>=60):
        result=minHour/60
        print(result)
    else:
        print("error")

def prac3(word):
    result = len(word)
    print(result) 

prac1(1)
prac2(1)
prac2(60)
prac3("happy")


