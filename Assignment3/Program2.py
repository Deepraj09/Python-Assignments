# 2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

# Input: Number of Elements: 7
# Input elements: 13 7 5 45 7 4 56 34
# Output: 56

def Maximum(Num):

    maxX = Num[0]
    for y in Num:
        if y > maxX:
            maxX = y
    return maxX


def main():
    print("Enter the size of the list : ",end = " ")
    size = int(input())

    Arr = []

    print("Enter the elements : ")

    for i in range(size):
        No = int(input())
        Arr.append(No)

    print("Entered elements in the list are : ",Arr)

    Result = Maximum(Arr)
    print("Maximum element from the list are : ",Result)

if __name__=="__main__":
    main()