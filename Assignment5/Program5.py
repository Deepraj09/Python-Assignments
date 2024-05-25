# 5. Write a recursive program which accept number from user and return its factorial.

# Input: 5
# Output: 120

def DisplayFact(Num):
    if Num < 0:
        return None
    elif Num == 0 or Num == 1:
        return 1
    else:
        return Num * DisplayFact(Num - 1)

def main():
    print("Enter the Frequency : ",end = " ")
    No = int(input())
    
    result = DisplayFact(No)
    if result is None:
        print("ERROR : Factorial is not defined for negative number.")
    else: 
        print("The factorial of", No, "is", result)

if __name__ == "__main__":
    main()