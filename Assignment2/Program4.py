# Write a program which accept one number form user and return addition of its factors.
# Input: 12     Output: 16     (1+2+3+4+6)

def Display(Num):

    if(Num == 1):
        return 1

    elif(Num > 0):
        Sum = 0
        for i in range(1, Num):
            if(Num % i == 0):
                print(i)
                Sum = Sum + i
        return Sum
    else:
        Sum = 0
        for i in range(Num + 1, 0):
            if(Num % i == 0):
                print(i)
                Sum = Sum + i
        return Sum
            

def main():
    print("Enter the number: ",end = " ")
    No = int(input())
    
    if(No == 1):
        Result = Display(No)
        print("The factor of the 1 is itself ",Result)

    elif(No > 0):
        print("The Positive factors of the numbers are : ")
        Result1 = Display(No)
        print("Addition of the Positive factors is : ", Result1)

    else:
        print("The Negative factors of the number are : ")
        Reuslt2 = Display(No)
        print("Addition of Negative factors is : ",Reuslt2)

if __name__ == "__main__":
    main()