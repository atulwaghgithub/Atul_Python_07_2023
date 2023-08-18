# Create an module named as Arithmatic which contains 4 Function as Add() for addition , Sub() for Subtraction
# ,Mult() for Multiplication and Div() for Division. all function accept two parameter as a number and perform 
# the operation write a python program  which call all function from arithmatic module by accepting the parameter
# from user

import Arithmatic
def main():

    No1 = 0
    No2 = 0
    iRet = 0

    print("Enter First Number")
    No1 = int(input())
    
    print("Enter Second Number")
    No2 = int(input())
    

    iRet = Arithmatic.Add(No1,No2)
    print("Addition is:",iRet)

    iRet = Arithmatic.Sub(No1,No2)
    print("Substraction is:",iRet)

    iRet = Arithmatic.Mult(No1,No2)
    print("Multiplication is:",iRet)

    iRet = Arithmatic.Div(No1,No2)
    print("Division is:",iRet)


if __name__ == "__main__":
    main()

