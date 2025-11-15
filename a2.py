def factorial(n):
    if n==0 :
        return 1 
    else:
        return n*  factorial(n-1)
    




num = int(input("enetr your number   "))
print("the factorial is  ", factorial(num))