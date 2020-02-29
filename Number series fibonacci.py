# Python Fibonacci series

def Fibonacci_series(Number):
           if(Number == 0):
                      return 0
           elif(Number == 1):
                      return 1
           else:
                      return (Fibonacci_series(Number - 2)+ Fibonacci_series(Number - 1))



Number = int(input("\nPlease Enter the Range Number: "))


for Num in range(0, Number):
           print(Fibonacci_series(Num))
