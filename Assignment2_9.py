
# Write a program which accept number from user and return number of digit in that number
# input 1234567
# Output 7

def DigitCount(No1):
    count = 0
    while(No1>0):
        No1 = No1//10
        count = count+1   
    return count    
        
def main():
    
    print("Enter a number")
    Value1 = int(input())

    ret = DigitCount(Value1)
    print("Number of digit is",ret)

if __name__ == "__main__":
       main()

