# 6. Write a program which accept one number and display below pattern.
# Input:  5
# Output: 1 2 3 4 5
#         1 2 3 4 5
#         1 2 3 4 5 
#         1 2 3 4 5
#         1 2 3 4 5

def Display(Num):
    for i in range(Num):
        for j in range(1, Num + 1):
            print(j, end = " ")
        print()

def main():
    print("Enter the Frequency : ",end = " ")
    No = int(input())

    Display(No)
if __name__ == "__main__":
    main()

