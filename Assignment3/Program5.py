# 5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
# Input: Number of elements: 11
# Input Elements: 13 5 45 7 4 56 10 34 2 5 8
# Output: 32  # (13+5+7+2+5)

import MarvellousNum as M

def ListPrime(No):
    sum = 0
    for ele in No:
        if M.ChkPrime(ele):
            sum = sum + ele
    return sum
    

def main():
    print("Enter the size of list : ")
    size = int(input())

    Arr = []

    print("Enter the elements : ")
    for i in range(size):
        No = int(input())
        Arr.append(No)

    print("Entered elements in the list are : ",Arr)

    Result = ListPrime(Arr)
    print("Summantion of the prime numbers are : ",Result)

if __name__ == "__main__":
    main()