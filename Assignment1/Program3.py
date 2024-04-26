# 3. Write a program which contains one function named as Add() which accepts two numbers. from user and return addition of that two numbers.
# Input: 11 5
# Output: 16

def Add(Num1, Num2):
    Ans = 0
    Ans = Num1 + Num2
    return Ans

def main():
    print("Enter the First number : ")
    No1 = int(input())

    print("Enter the Second number : ")
    No2  = int(input())

    Result = Add(No1, No2)

    print("Addition of two numbers is : ", Result)

if __name__ == "__main__":
    main()