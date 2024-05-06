# 1. Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input: 4       Output: 16
# Input: 8       Output: 64

Square = lambda Num : Num ** 2

def main():
    print("Enter the Number : ",end = " ")
    No = int(input())

    Result = Square(No)
    print("Square of the {} is {}".format(No, Result))

if __name__ == "__main__":
    main()