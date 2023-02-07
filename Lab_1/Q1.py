#Lab 1 Q1 SUM OF INPUT NUMBERS

def main():
    inputs = input("Enter two or more numbers: (separate with spaces)")

    numbers = inputs.split(" ")
    # print(numbers)
    # print(type(numbers))
    sum = 0
    for i in numbers:
        try:
            num = float(i)
            sum += num
        except ValueError:
            print("\nYou entered a string!! Program ended.\n")
            exit(1)
    print("The sum of the numbers is: ",sum)

if __name__ == '__main__':
    main()