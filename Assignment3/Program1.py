# 1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input: Number of elements: 6 
# Input Elements: 13 5 45 7 4 56
# Output: 130


def Addition(Num):
    Sum = 0

    for no in Num:
        Sum = Sum + no
    return Sum

def main():
    print("Enter the size of list : ",end = " ")
    size = int(input())
    
    Arr = []        # Arr = list() or Arr = []

    print("Enter the elements : ")

    for i in range(size):
        No = int(input())
        Arr.append(No)

    print("Entered elements are : ",Arr)

    Result = Addition(Arr)
    print("Summation of elements is : ", Result)


if __name__ == "__main__":
    main()