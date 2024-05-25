# 1. Write a recursive program which display below pattern.

# Input:   5
# Output:  * * * * * 


def Display(Num):
    if(Num == 0):
        return
    print(" * ",end = " ")
    Display(Num - 1)

def main():
    
    print("Enter the number : ",end = " ")
    No = int(input())

    Display(No)
if __name__ == "__main__":
    main()