# 1. Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for for division. 
# All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

from Program1 import *

def main():
    print("Enter the First number : ",end = " ")
    No1 = int(input())

    print("Enter the Second Number : ",end = " ")
    No2 = int(input())

    aRet = Add(No1, No2)
    print("Addition is : ",aRet)

    mRet = Mul(No1, No2)
    print("Multiplication is : ",mRet)

    dRet = Div(No1, No2)
    print("Division is : ",dRet)

    sRet = Sub(No1, No2)
    print("Substraction is : ",sRet)

if __name__ == "__main__":
    main()