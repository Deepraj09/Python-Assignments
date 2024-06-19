
# Assignment: 7
# 1. Write a program which contains one class named as Demo.
# Demo class contains two instance variables as no1, по2.
# That class contains one class variable as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance variables.
# Initialise instance variable in init method by accepting the values from user.
# After creating the class create the two objects of Demo class as
# Obj1 Demo(11,21) 
# Obj2 Demo(51,101)
# Now call the instance methods as 
# Obj1.Fun()
# Obj2.Fun() 
# Obj1.Gun()
# Obj2.Gun()

class Demo:
    Value = 0 # Class variable

    def __init__(self, No1, No2):
        self.No1 = No1   # Instance variable
        self.No2 = No2   # Instance variable

    def Fun(self):       # Instance Method
        print("Inside Fun")
        self.Value = self.No1   # Class variable in instance method
        print(self.Value)
        self.Value = self.No2
        print(self.Value)

    def Gun(self):       # Instance Method
        print("Inside Gun")
        self.Value = self.No1   # Class variable in instance method
        print(self.Value)
        self.Value = self.No2
        print(self.Value)

def main():
    print("------------- Demonstration of the Class ---------------------")

    print("Enter the Number1 for obj1: ",end = " ")
    No1 = int(input())

    print("Enter the Number2 for obj1: ",end = " ")
    No2 = int(input())

    obj1 = Demo(No1, No2)

    print("Enter the Number1 for obj2: ",end = " ")
    No1 = int(input())
    
    print("Enter the Number2 for obj2: ",end = " ")
    No2 = int(input())

    obj2 = Demo(No1, No2)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()