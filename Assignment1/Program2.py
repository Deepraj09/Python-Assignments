# Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.
# Input: 11
# Input: 8
# Output: Odd Number
# Output: Even Number

def ChkNum(num):
    if(num < 0):
        print("Invalid Number")
    elif (num % 2 == 0):
        print("Given input is even number")
    else:
        print("Given input is odd number")

def main():
    print("Enter the Number : ")
    No1 = int(input())
    
    ChkNum(No1)

if __name__ == "__main__":
    main()