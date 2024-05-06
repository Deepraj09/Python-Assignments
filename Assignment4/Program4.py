# 4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
# List after filter = [2, 4, 4, 2, 8, 10] 
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

from functools import reduce

ListEven = lambda No : No % 2 == 0

ListSquares = lambda No : No**2

ListAdd = lambda A, B : A + B

def main():
    print("Enter the size of list : ",end = " ")
    size = int(input())

    Arr = []

    print("Enter the elements : ")
    for i in range(size):
        No = int(input())
        Arr.append(No)

    print("Entered elements in the list are : ",Arr)

    FArr = list(filter(ListEven, Arr))
    print("List after filter : ",FArr)

    MArr = list(map(ListSquares, FArr))
    print("List after map : ",MArr)

    RArr = reduce(ListAdd, MArr)
    print("Output after reduce : ",RArr)

if __name__ == "__main__":
    main()