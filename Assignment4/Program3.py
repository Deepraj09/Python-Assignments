# 3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70] 
# List after map [86, 99, 96, 100, 80] 
# Output of reduce = 6538752000

from functools import reduce

LtGt = lambda No : No >= 70 and No <= 90

Increase = lambda No : No + 10

Prod = lambda No1, No2 : No1*No2

def main():
    print("Enter the size of list : ")
    size = int(input())

    Arr = []

    print("Enter the elements : ")
    for i in range(size):
        No = int(input())
        Arr.append(No)

    print("Entered Numbers are : ",Arr)

    LTArr = list(filter(LtGt, Arr))
    print("List after filter : ",LTArr)

    MArr = list(map(Increase, LTArr))
    print("List after map : ",MArr)

    PArr = reduce(Prod, MArr)
    print("Output of  reduce is : ",PArr)
    

if __name__ == "__main__":
    main()