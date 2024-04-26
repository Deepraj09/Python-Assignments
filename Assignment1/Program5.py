# 5. Write a program which display 10 to 1 on screen.
# Output: 10
# 9 
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

def Display(Num):
    for i in range(Num,0,-1):
        print(i)


def main():
    print("Enter the Frequecy : ", end=" ")
    No = int(input())

    Display(No)

if __name__ == "__main__":
    main()