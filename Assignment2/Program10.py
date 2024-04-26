# 10. Write a program which accept number from user and return addition of digits in that number.
# Input: 5187934
# Output: 37

def GetSum(Num):
    if(Num < 0):
        return -1
    else:
        Sum = 0
        while(Num != 0):
            Sum = Sum + (Num % 10)
            Num = Num // 10
        return Sum

def main():
    print("Enter the number : ",end = " ")
    No = int(input())

    Result = GetSum(No)
    print("Addition of the digits is : ", Result)

if __name__ == "__main__":
    main()