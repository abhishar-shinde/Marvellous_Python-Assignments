def fun():
    print("Hello From Fun")

fun()

def ChkNum():
    num = int(input("Enter Number: "))
    if num % 2:
        print("Even Number: ", num)
    else:
        print("Odd Number: ", num)
        
ChkNum()

def addition():
    value1 = int(input("Enter Number First: "))
    value2 = int(input("Enter Second First: "))
    
    return value1 + value2

addition()


def LoopMarvellous():
    for i in list(range(5)):
        print("Marvellous")
        
        
LoopMarvellous()

def ReversNumber():
    for i in list(range(10,0,-1)):
        print(i)
        
ReversNumber()

def CheckPositiveNegativeNumbers():
    number = int(input("Enter Number: "))
    
    if number < 0:
        print("Negative Number")
    elif number > 0:
        print("Positivie Number")
    else:
        print("Zero")

CheckPositiveNegativeNumbers()

def CheckIfFunctionIsDividedByFive():
    number = int(input("Enter Number: "))
    
    if number / 5 == 0:
        print("Divided By 5")
        return True
    else :
        return False
    
CheckIfFunctionIsDividedByFive()

def PrintStar():
    number = int(input("Enter Number: "))
    for i in list(range(number)):
        print("*")
        
PrintStar()     

def PrintEvenNumbers():
    for i in list(range(2,22,2)):
        print(i)
        
PrintEvenNumbers()


def DisplayLength():
    name = input("Enter You Name: ")
    print(len(name))
    
DisplayLength()

    
    