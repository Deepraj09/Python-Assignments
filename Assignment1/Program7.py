# Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.
# Input: 8
# Input: 25
# Output: False
# Output: True

def Check(Num):
    iAns = Num % 5
    if Num < 0:
        return "Invalid Input"
    elif(iAns == 0):
        return True
    else:
        return False
    

def main():
   

    print("Enter the number : ",end = " ")
    No = int(input())

    bRet = Check(No)
    print(bRet)

if __name__ == "__main__":
    main()