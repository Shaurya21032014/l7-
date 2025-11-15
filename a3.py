def add(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


print("enetr your choice")
print(" 1 add")
print("2 substract")
print("3 multiply")
print("4  division")


choice =input("enter your choice")


num1 = int(input("enter your number"))
num2 = int(input("enter your number"))






if choice == "1":
    print("res", add(num1,num2))
elif choice == "2":
    print("res", substract(num1,num2))
elif choice == "3":
    print("res", multiply(num1,num2))
elif choice == "4":
    print("res", division(num1,num2))
else:
    print("invalud choice ")


