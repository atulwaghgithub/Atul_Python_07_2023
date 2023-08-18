
#  Write a program which accept Number from user and check whether that number is postive or negative or zero

def Positive(Value):
    if(Value > 0):
        print("Positive")
    elif(Value == 0):
        print("Zero") 
    else:
        print("Negative")

def main():
    No = 0
    print("Enter Number")
    No = int(input())

    Positive(No)

if __name__ == "__main__":
    main()
