# 8. Write a program which accept number from user and print that number of "*" on screen.
# Input: 5
# Output: * * * * *

def Pattern(Num):
    for i in range(Num):
        print(" * ",end = " ")

def main():
    print("Enter the Frquency : ")
    No = int(input())

    Pattern(No)

if __name__ == "__main__":
    main()