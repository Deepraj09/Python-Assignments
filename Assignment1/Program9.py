# 9. Write a program which display first 10 even numbers on screen 
# Output:
# 2
# 4
# 6 
# 8 
# 10
# 12
# 14
# 16
# 18
# 20

def Display(Num):

    for i in range(Num, 21, 2):
        print(i)

def main():
    print("Enter the Frequecy : ",end = " ")
    No = int(input())

    Display(No)
if __name__ == "__main__":
    main()

