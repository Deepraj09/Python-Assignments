# 6. Write a program which accept number from user and check whether that number is positive or negative or zero.
# Input: 11
# Input: -8
# Input: 0
# Output: Positive Number Output: Negative Number
# Output: Zero

def ChkNum(Num):
    if(Num < 0):
        print("Given input is Negative")
    elif(Num == 0):
        print("Given input is Zero")
    else:
        print("Given input is Positive")
    
def main():
    print("Enter the Number : ",end = " ")
    No = int(input())

    ChkNum(No)

if __name__ == "__main__":
    main()