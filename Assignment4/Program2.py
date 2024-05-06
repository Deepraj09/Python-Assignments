# 2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input: 4  3   Output: 12
# Input: 6  3   Output: 18


Mul = lambda Num1, Num2 : Num1 * Num2

def main():
    print("Enter the First Number : ",end = " ")
    No1 = int(input())

    print("Enter the Second Number : ",end = " ")
    No2 = int(input())

    Result = Mul(No1, No2)
    print("Multiplication of the numbers is : ",Result)

if __name__ == "__main__":
    main()