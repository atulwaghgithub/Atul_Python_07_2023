# Write a program which accept one number and display below pattern
# Input : 5
# Output: 
#            1  2  3  4  5
#            1  2  3  4  5 
#            1  2  3  4  5
#            1  2  3  4  5
#            1  2  3  4  5


def Pattern(No1):
    for i in range(1,No1+1):
        for j in range(1,No1+1):
            print(j,end="   ")
        print()     
    

def main():
    Value1 = 0
    print("Enter a number")
    Value1 = int(input())

    Pattern(Value1)

if __name__ == "__main__":
       main()

