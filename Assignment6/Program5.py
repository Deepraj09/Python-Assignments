# Design python application which contains two threads named as thread1 and thread2.
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
# screen. After execution of thread1 gets completed then schedule thread2.

import threading
import time

def Thread1(Num):
    print(f"Numbers from 1 to {Num} are: ")
    for i in range(1,Num + 1):
        print(i)
        time.sleep(0.1)

def Thread2(Num):
    print(f"Numbers from {Num} to 1 is: ")
    for i in range(Num, 0, -1):
        print(i)
        time.sleep(0.1)

def main():
    print("------------- MultiThreading Application --------------------")

    print("Enter the Number: ")
    No = int(input())

    p1 = threading.Thread(target= Thread1, args= (No,))
    p2 = threading.Thread(target= Thread2, args= (No,))

    # start Thread1
    p1.start()

    # Wait for thread1 to complete execution
    p1.join()

    # start Thread2
    p2.start()
    
    # Wait for thread to complete execution
    p2.join()

    print("End of main process")

if __name__ == "__main__":
    main()