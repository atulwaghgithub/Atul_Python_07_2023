# Write a Program which accept number from user and that number of "*" on screen.

def star(Value):
    data = range(0,Value,1)
    for no in data:
        no = no+1
        print("*",end="   ")


def main():
    no = 0
    print("Enter Number")
    no = int(input())

    star(no)




if __name__ == "__main__":
    main()
