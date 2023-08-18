
# Wrie a programwhich  Accept number from user and return  Addition of digit in that number
# input : 5187934
# OutPut : 37

def CountDigitAddition(No1):
    count = 0
    Ans = 0
    while(No1>0):
        No1 = No1//10
        count = count+1
        Ans = Ans + count  
    return Ans    
        

def main():
    Value1 = 0
    print("Enter a number")
    Value1 = int(input())

    ret = CountDigitAddition(Value1)
    print(" digit Addition  is",ret)

if __name__ == "__main__":
       main()

