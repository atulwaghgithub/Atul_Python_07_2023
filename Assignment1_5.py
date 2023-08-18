# write a program which display 10 to 1 number on screen.

def DipalyNumber():
    data = range(10,1,-1)
    for no in data:
        no = no-1
        print(no)
def main():

    DipalyNumber()
    
if __name__ == "__main__":
    main()
