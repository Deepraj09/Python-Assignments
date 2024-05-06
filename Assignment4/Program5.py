# 5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
# Input List = [2, 70, 11, 10, 17, 23, 31, 77] 
# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 621]

from functools import reduce

def isPrime(No):
    if No <= 1:
        return False
    for i in range(2, int(No // 2) + 1):
        if No % i == 0:
            return False
    return True

Mul = lambda No : No * 2

ListMax = lambda No1, No2 : max(No1, No2)

def main():
    print("Enter the size of list : ",end = " ")
    size = int(input())

    Arr = []

    print("Enter the elements : ")
    for i in range(size):
        No = int(input())
        Arr.append(No)

    print("Entered elements in the list are : ",Arr)

    FArr = list(filter(isPrime, Arr))
    print("List after filter : ",FArr)

    MArr = list(map(Mul, FArr))
    print("List after map : ",MArr)

    RArr = reduce(ListMax, MArr)
    print("Output after reduce : ",RArr)

if __name__ == "__main__":
    main()