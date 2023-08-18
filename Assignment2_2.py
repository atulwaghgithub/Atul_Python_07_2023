
# write a program which accept one number and display below pattern

# Input : 5
# Output  : 

#            *  *  *  *  *
#            *  *  *  *  *
#            *  *  *  *  *
#            *  *  *  *  *
#            *  *  *  *  *

def Pattern(No1):

    for i in range(No1):
        for j in range(No1):
            print("*",end="   ")
        print()     
    

def main():
    print("Enter a number")
    Value1 = int(input())

    Pattern(Value1)

if __name__ == "__main__":
 main()
