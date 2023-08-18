# Write a program which accept one number and display below pattern
# Input : 5
# Output: 
#            1           
#            1  2         
#            1  2  3    
#            1  2  3  4  
#            1  2  3  4  5

def Pattern(No1):
    for i in range(No1+1):
        for j in range(1,i+1,1):
            print(j,end="   ")
        print()     
    

def main():
    print("Enter a number")
    Value1 = int(input())

    Pattern(Value1)

if __name__ == "__main__":
       main()

