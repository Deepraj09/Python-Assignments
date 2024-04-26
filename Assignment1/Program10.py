# Write a program which accept name from user and display length of its name.
# Input: Marvellous       Output: 10

def Display(Str1):
    return len(Str1)


def main():
    print("Enter the name : ")
    Str = input()

    Ans = Display(Str)

    print("Length of the string is : ", Ans)

if __name__ == "__main__":
    main()