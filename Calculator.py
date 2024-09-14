first_var=int(input("Enter the first number: "))
second_var=int(input("Enter the second variable: "))
check=input("Please Press + , - , * , / \n")
if check=='+':
    print("You are performing addition")
    first_var+=second_var
    print("=",first_var)

elif check=='-':
    print("You are performing Substraction")
    first_var-=second_var
    print("=",first_var)

elif check=='*':
    print("You are performing Multiplication")
    first_var*=second_var
    print("=",first_var)

elif check=="/":
    print("You are performing Division")
    first_var/=second_var
    print("=",first_var)

