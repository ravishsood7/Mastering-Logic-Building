#1. Write a program to check whether a number is positive, negative, or zero.

def number(num):
    if num > 0:
        return "Positive Number"
    elif num < 0:
        return "Negative Number"
    else:
        return "Zero"


if __name__ =="__main__":
    while(True):
        numb = int(input("Enter the number"))
        val = number(numb)
        print(f"Entered number {numb} is -> {val}")

        print("\n Do you want to continue")
        choice = input("Enter Y/N")
        if choice =="Y":
            continue
        else:
            break
