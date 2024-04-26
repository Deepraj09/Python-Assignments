# 6. Write a program which accept one number and display below pattern.
# Input:  5
# Output: * * * * * 
#         * * * * 
#         * * *
#         * *
#         *

def Display(Num):
    for i in range(Num):
        for j in range(1, Num - i + 1):
            print(" * ",end = " ")
        print()

def main():
    print("Enter the Frequency : ",end = " ")
    No = int(input())

    Display(No)
if __name__ == "__main__":
    main()

