# 9. Write a program which accept number from user and return number of digits in that number.
# Input: 5187934   Output: 7

def CntDigit(Num):
    if(Num == 0):
        return 1
    Cnt = 0
    while(Num != 0):
        Num //= 10
        Cnt = Cnt + 1
    return Cnt
        

def main():
    print("Enter the Digits : ",end = " ")
    No = int(input())

    Result = CntDigit(No)
    print("Lenght of Digits is : ", Result)

if __name__ == "__main__":
    main()