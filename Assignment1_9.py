# Write a program which display first 10 even on screen

def DisplayEven():
    data = range(0,20,1)
    for no in data:
        no = no+1
        Result = 0
        Result = no % 2
        if(Result == 0):
            print(no)
        
def main():

    DisplayEven()

if __name__ == "__main__":
    main()
