
def Add(Value1,Value2):
    iAns = 0
    iAns = Value1+Value2
    return iAns



def main():
 No1 = 0
 No2 = 0
 iRet =0
 print("Enter first Number")
 No1 = int(input())

 print("Enter Second Number")
 No2 = int(input())

 iRet = Add(No1,No2)
 print("Addition is:",iRet)


if __name__ == "__main__":
 main()

