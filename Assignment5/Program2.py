# 2. Write a recursive program which display below pattern.
# Input:   5
# Output:  1 2 3 4 5

def Display(Num):
    if(Num == 0):
        return 
    Display(Num - 1)
    print(Num,end = " ")


def main():
    print("Enter the Frequecny : ",end = " ")
    No = int(input())

    Display(No)
if __name__ == "__main__":
    main()