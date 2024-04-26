# 5. Write a program which accept one number for user and check whether number is prime or not.
# Input:  5
# Output: It is Prime Number

def ChkPrime(Num):
    if(Num < 0):
        return "Invalid Input"
    
    for i in range(2,Num):
        if(Num % i == 0):
            return False
        else:
            return True

def main():
    bRet = False
    print("Enter the number: ")
    No = int(input())

    bRet = ChkPrime(No)
    if(bRet == True):
        print("The Given input is prime Number ")
    else:
        print("The Given input is not a prime Number")

if __name__ == "__main__":
    main()