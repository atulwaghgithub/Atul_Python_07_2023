# Write a program which accept one number from user and return factroial 
# input : 5 
# Output : 120

def Factorial(No):
    data = 1
    for i in range(1,No+1):
        data = data * i
    return data   

def main():
    Value = 0
    iRet = 0 

    print("Enter a number")
    Value = int(input())
    
    iRet = Factorial(Value)
    print("Factioal is",iRet)
    
if __name__ == "__main__":
    main()
  
  