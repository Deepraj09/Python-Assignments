# 3. Write a program which contains one class named as Arithmetic. Arithmetic class contains three instance variables as Value1, Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside class as Accept(), Addition(), Subtraction(), Multiplication(), Division().
# Accept method will accept value of Value1 and Value2 from user. Addition() method will perform addition of Value1, Value2 and return result.
# Subtraction() method will perform subtraction of Value1, Value2 and return result. Multiplication() method will perform multiplication of Value1, Value2 and return result. 
# Division() method will perform division of Value1, Value2 and return result. After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter First Number: ",end = " ")
        self.Value1 = float(input())

        print("Enter Second Number: ",end = " ")
        self.Value2 = float(input())

    def Addition(self):
        Result = self.Value1 + self.Value2
        return Result
    
    def Substraction(self):
        Result = self.Value1 - self.Value2
        return Result

    def Multiplication(self):
        Result = self.Value1 * self.Value2
        return Result 

    def Division(self):
        if self.Value2 != 0:
            Result = self.Value1 / self.Value2
        else:
            Result = "Division by Zero is not defined"
        return Result

def main():
    print("---------- Demonstration of class ------------------")

    obj1 = Arithmetic()

    obj1.Accept()
    Result = obj1.Addition()
    print("Addition is : ",Result)

    Result = obj1.Substraction()
    print("Substraction is : ",Result)

    Result = obj1.Multiplication()
    print("Multiplication is : ",Result)

    Result = obj1.Division()
    print("Division is : ",Result)
    

if __name__ == "__main__":
    main()   
        
