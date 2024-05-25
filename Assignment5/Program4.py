# 4. Write a recursive code in python which accept number from user and return summation of its digits.

# Input : 879
# Output : 24

def DisplaySum(Num):
    if(Num == 0):
        return 0
    return int(Num % 10) + DisplaySum((Num / 10))

def main():
    print("Enter the number : ",end = " ")
    No = int(input())

    result = DisplaySum(No)
    print("The Summation of its digits is : ",result)
if __name__ == "__main__":
    main()