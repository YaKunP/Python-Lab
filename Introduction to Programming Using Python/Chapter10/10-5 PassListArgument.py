def main():
    x = 1    # x is an int variable
    y = [1, 2, 3]    # y is a list

    m(x, y)    # Invoke m with arguments x and y

    print("x is", x)
    print("y[0] is", y[0])

def m(number, numbers):
    number = 1001    # Assign a new value to number
    numbers[0] = 5555    # Assign a new value to numbers[0]

main()    # Call the main function
