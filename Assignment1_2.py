# Write a program which contain one fnction named as ChkNum() which accept one prameter as a number 
# if number is even then it should display "Even Number" otherowise Display "Odd Number" on console.

def ChkNum(Value):
    Result = 0
    Result = Value % 2
    if(Result == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    No = 0
    print("Enter Number")
    No = int(input())

    ChkNum(No)

    
if __name__ == "__main__":
    main()