# Problem:- Design python application which creates two thread named as even and odd. 
#           Even Thread will display first 10 even numbers and odd thread wil dispaly 
#           first 10 odd numbers.
#           Input:- 10
#           Output:- List of even numbers :
#           Even :  2
        #   Even :  4
        #   Even :  6
        #   Even :  8
        #   Even :  10
        #   Even :  12
        #   Even :  14
        #   Even :  16
        #   Even :  18
        #   Even :  20
        #   List of odd numbers :
        #   Odd :  1
        #   Odd :  3
        #   Odd :  5
        #   Odd :  7
        #   Odd :  9
        #   Odd :  11
        #   Odd :  13
        #   Odd :  15
        #   Odd :  17
        #   Odd :  19

import threading

def DisplayEven(Num):
    print("List of even numbers: ")
    x = 2
    for i in range(Num):
        print("Even: ",x)
        x = x + 2

def DisplayOdd(Num):
    print("List of odd Numbers is: ")
    x = 1
    for i in range(Num):
        print("Odd : ",x)
        x = x + 2

def main():
    print("---------- Thread application ----------------")


    print("Enter the Range till where you want to print even and odd numbers: ",end = " ")
    No = int(input())

    p1 = threading.Thread(target = DisplayEven, args = (No, ))
    p2 = threading.Thread(target= DisplayOdd, args = (No, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")


if __name__ == "__main__":
    main()