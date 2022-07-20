def prac1(numOfHours):
    result = int(input("number of hours "))
    print(result*60)

def prac2(run):
    hr_min = (input("enter H or M "))
    minHour = int(input("enter number "))
    if(hr_min=="H"):
        result=minHour*60
        print(result)
    elif(hr_min=="M"):
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


