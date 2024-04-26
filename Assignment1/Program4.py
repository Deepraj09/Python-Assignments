# 4. Write a program which display 5 times Marvellous on screen.
# Output:
# Marvellous
# Marvellous 
# Marvellous
# Marvellous
# Marvellous

def Display(Num1):
    for i in range(Num1):
        print("Marvellous")

def main():
    print("Enter the Frequency : ")
    No1 = int(input())

    Display(No1)

if __name__ == "__main__":
    main()