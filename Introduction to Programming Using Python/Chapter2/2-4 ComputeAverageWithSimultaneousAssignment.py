# Prompt the user to enter three numbers
number1, number2, number3 = eval(input("Enter three numbers separated by commas: "))

# Compute average
average = (number1 + number2 + number3) / 3

# Display result
print("The average of", number1, number2, number3, "is", average)



'''
    Note:
        使用常量有三个好处：
            1. 你不必为使用一个值多次而重复性输入
            2. 如果需要修改常量的值，只需要在源代码一处进行修改
            3. 描述性名字会提高程序的易读性
'''