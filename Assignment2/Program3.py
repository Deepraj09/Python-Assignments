# 3. Write a program which accept one number from user and return its factorial.
# Input: 5
# Output: 120

def Fact(Num):
    if(Num < 0):
        return "Invalid Input"
    elif(Num == 0 or Num == 1):
        return 1
    else:
        fact = 1
        for i in range(1, Num + 1):
            fact = fact * i
        return fact 
        

def main():
    print("Enter the Number : ",end = " ")
    No = int(input())

    Result = Fact(No)
    print("Factorial of the number is : ",Result)

if __name__ == "__main__":
    main()