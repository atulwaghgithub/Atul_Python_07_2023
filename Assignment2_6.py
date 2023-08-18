
#  Write a program which accept one number and display  below pattern.
# input : 5
# Output :   
#            *  *  *  *  *
#            *  *  *  *
#            *  *  *
#            *  *
#            *

def Pattern(No1):
    for i in range(No1,0,-1):
        for j in range(0,i,1):
            print("*",end="   ")
        print()     
    

def main():
    Value1 = 0
    print("Enter a number")
    Value1 = int(input())

    Pattern(Value1)

if __name__ == "__main__":
       main()

