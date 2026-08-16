# Program to add two number in python
def add(num1,num2):
    return num1 + num2


if __name__ =="__main__":
    while(True):
        num1 = int(input("Enter the First Number: "))
        num2 = int(input("Enter the Second Number: "))

        sum = add(num1, num2)
        print(f"{num1} + {num2} = {sum} \n")

        choice = input("Do you want to continue : y/n")

        if choice.lower() == "y":
            continue
        else:
            break