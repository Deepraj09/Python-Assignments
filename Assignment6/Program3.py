#   Design python application which creates two threads as evenlist and oddlist. Both the threads accept list of integers
#   as parameter. Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd
#   elements from the input list and display the addition

import threading

def Evenlist(No):
    Sum = 0
    for num in No:
        if(num % 2 == 0):
            print("Even Numbers: ",num)
            Sum = Sum + num
    print("Addition of Even numbers is : ",Sum)

def Oddlist(No):
    Sum = 0
    for num in No:
        if(num % 2 != 0):
            print("Odd Numbers: ",num)
            Sum = Sum + num
    print("Addition of Odd numbers is : ",Sum)

def get_user_input():
    input_string = input("Enter the elements seprated by space: ")
    return list(map(int, input_string.split()))

def main():
    print("---------- MultiThreading application ----------------")

    No = get_user_input()

    p1 = threading.Thread(target= Evenlist, args= (No,))
    p2 = threading.Thread(target= Oddlist, args= (No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()

