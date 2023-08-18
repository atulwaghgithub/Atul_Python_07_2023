# Write a program which accept one number from user and return addition of its factor.
# Input : 12
# Output : 16    (1+2+3+4+6)

def FactorAddition(Value):
    Ans = 0
    for i in range(1,Value,1):
        if(Value % i) == 0 :
         Ans = Ans + i
    return Ans     
         
    
def main():
    No = 0
    iRet = 0
    print("Enter number")
    No = int(input())

    iRet = FactorAddition(No)
    print("Addition of Factor is:",iRet)

if __name__ == "__main__":
    main()

