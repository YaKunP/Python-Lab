# Receive an input
number = eval(input("Enter an integer: "))

if number % 2 == 0 and number % 3 == 0:
    print(number, "is divisible by 2 and 3")

if number % 2 == 0 or number % 3 == 0:
    print(number, "is divisible by 2 or 3")

if (number % 2 == 0 or number % 3 == 0) and \
    not (number % 2 == 0 and number % 3 == 0):
    print(number, "is divisible by 2 or 3, but not both")





    '''
    德摩根律，可以用来简化布尔表达式，定理陈述的是：
    
    not(condition1 and condition2) 和 condition or not condition2 一样
    
    not(condition1 or condition2) 和 not condition1 and not condition2 一样
    '''