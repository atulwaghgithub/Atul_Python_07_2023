
# write a program which contain one function that accept one number from user and return true if number
# Divisible by 5 otherwise return false

def Div(Value):
    Result = 0
    Result = Value % 5
    if(Result ==0):
        print("True")
    else:
        print("False")    

def main():

    No = 0 
    print("Enter Number")
    No = int(input())
    Div(No)

if __name__ == "__main__":
    main()
