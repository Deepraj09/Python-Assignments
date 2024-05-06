# 4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
# Input: Number of elements: 11
# Input Elements: 13 5 45 7 4 56 5 34 2 5 65
# Element to search: 5
# Output: 3

def Frequency(list1, No):
    Cnt = 0
    for ele in list1:
        if(ele == No):
            Cnt = Cnt + 1
    return Cnt
    

def main():
    print("Enter the size of list : ",end = " ")
    size = int(input())

    Arr = []

    print("Enter the elements : ")
    for i in range(size):
        No = int(input())
        Arr.append(No)

    print("Entered elements in the list are : ",Arr)

    print("Enter the Element to search : ")
    No1 = int(input())

    Result = Frequency(Arr, No1)
    print("Element {} occurs for the {} time".format(No1,Result))

if __name__ == "__main__":
    main()