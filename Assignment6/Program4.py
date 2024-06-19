# Design python application which creates three threads as small, capital, digits. All the
# threads accepts string as parameter. Small thread display number of small characters,
# capital thread display number of capital characters and digits thread display number of
# digits. Display id and name of each thread.

import threading

def Small(str):
    print("Thread ID: ",threading.get_ident())
    print("Thread Name: ",threading.current_thread().name)
    Sum = 0
    for c in str:
        if(c.islower()):
            print("Small char: ",c)
            Sum = Sum + 1
    print("Total Small character present in string is: ",Sum)

def Capital(str):
    print("Thread ID: ",threading.get_ident())
    print("Thread Name: ",threading.current_thread().name)
    Sum = 0
    for c in str:
        if(c.isupper()):
            print("Capital char: ",c)
            Sum = Sum + 1
    print("Total Capital character present in string is: ",Sum)

def Digit(str):
    print("Thread ID: ",threading.get_ident())
    print("Thread Name: ",threading.current_thread().name)
    Sum = 0
    for c in str:
        if(c.isdigit()):
            print("Digits : ",c)
            Sum = Sum + 1
    print("Total Digits present in string is: ",Sum)


def main():
    print("---------------- MultiThreading application ---------------")

    print("Enter the string as input: ")
    str = input()

    p1 = threading.Thread(target= Small, args= (str,))
    p2 = threading.Thread(target= Capital, args= (str,))
    p3 = threading.Thread(target= Digit, args= (str,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


if __name__ == "__main__":
    main()