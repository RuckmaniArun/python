print("This is my first calculator program")
def get_operation():
    print("""Enter user operation
    1. Addition
    2. Subtraction
    3.Multiplication
    4. Division..\n""")
    value1 = int(input("Enter the operation.."))
    return value1

def get_number(value):
    x = int(input("Give first number"))
    y = int(input("Give second number"))
    if value==1:
        return x+y
    elif value==2:
        return x-y
    elif value==3:
        return x*y
    elif value==4:
        return x/y
    else:
        print("Operation not available")
        return None

while True:
    print("I'm inside the loop")
    value=get_operation()
    print(get_number(value))
    flag=(input("do you want to use calculator again? Y/N:"))
    print(f"User final input:{flag}")
    if flag=="N":
        break