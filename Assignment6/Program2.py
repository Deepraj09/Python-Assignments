#   Design python application which creates two threads as evenfactor and oddfactor.
#   Both the thread accept one parameter as integer. Evenfactor thread will display
#   addition of even factors of given number and oddfactor will display addition of odd
#   factors of given number. After execution of both the thread gets completed main thread
#   should display message as exit from main

import threading

def DisplayEven(Num):
    Sum = 0
    for i in range(1, Num):
        if(Num % i == 0 and i % 2 == 0):
            print("Even factor: ",i)
            Sum = Sum + i
    print("Addition of Even factorials are: ",Sum)

def DisplayOdd(Num):
    Sum = 0
    for i in range(1, Num):
        if(Num % i == 0 and i % 2 != 0):
            print("Odd Factors: ",i)
            Sum = Sum + i
    print("Addition of Odd factors is: ",Sum)


def main():
    print("----------- MultiThreading Application ----------------")

    print("Enter the Number whose factorial addition you want to find: ",end = " ")
    No = int(input())

    p1 = threading.Thread(target= DisplayEven, args=(No,))
    p2 = threading.Thread(target= DisplayOdd, args=(No,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")

if __name__ == "__main__":
    main()