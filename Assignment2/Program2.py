# 2. Write a program which accept one number and display below pattern.
# Input: 5
# Output : * * * * *
#          * * * * *
#          * * * * *
#          * * * * *

def Pattern(Num):
    for i in range(Num):
        for j in range(Num):
            print(" * ", end = " ")
        print()

def main():
    print("Enter the Frequency : ",end = " ")
    No = int(input())

    Pattern(No)   
if __name__ == "__main__":
    main()