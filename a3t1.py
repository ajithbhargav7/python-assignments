num = int(input("enter the number to calculate factrial:"))
def factorial(n):
       if n>= 1:
           return n*factorial(n-1)
       else :
           return 1
print("factorial of",num,"is:",factorial(num))       