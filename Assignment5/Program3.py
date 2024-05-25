# 3. Write a recursive program which display below pattern.

# Input:   5
# Output:  5 4 3 2 1

def Display(Num):
    if(Num == 0):
        return
    print(Num,end = " ")
    Display(Num - 1)

def main():
    print("Enter the Frequency : ",end = " ")
    No = int(input())

    Display(No)
if __name__ == "__main__":
    main() 