
# Write a program which accept one number from user and check whether number is prime or not .
# Input : 5
# Output : It is prime Number

def PrimeNumber(Value):
    flag = 0
    for i in range(2,Value):
        if (Value % i) == 0:
            flag = 1
            break
    if(flag == 1):
        print("It is not Prime Number")
    else:
        print("it is prime number")            
     
def main():
    No = 0
    
    print("Enter number")
    No = int(input())

    PrimeNumber(No)
    

if __name__ == "__main__":
    main()

